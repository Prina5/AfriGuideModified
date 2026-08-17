from fastapi import APIRouter, Depends, HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from backend.auth import create_access_token, get_current_user
from backend.database import get_db
from backend.intent import detect_intent

from backend.model import (
    Conversation,
    ConversationMessage,
    Destination,
    DestinationFeature,
    Recommendation,
    User,
    UserPreference,
)

from backend.recommendation import generate_recommendations

from backend.schema import (
    ChatRequest,
    ChatResponse,
    ConversationCreate,
    ConversationMessageCreate,
    UserLogin,
    UserPreferenceCreate,
    UserRegister,
)

password_hash = PasswordHash.recommended()

router = APIRouter()


# ============================================================
# HOME
# ============================================================

@router.get("/")
def home():
    return {
        "message": "Welcome to AfriGuide AI"
    }


# ============================================================
# DESTINATIONS
# ============================================================

@router.get("/destinations")
def get_destinations(
    db: Session = Depends(get_db)
):
    """
    Return all destinations.
    """

    return db.query(Destination).all()


@router.get("/destinations/{destination_id}")
def get_destination(
    destination_id: int,
    db: Session = Depends(get_db)
):
    """
    Return one destination.
    """

    destination = (
        db.query(Destination)
        .filter(
            Destination.destination_id == destination_id
        )
        .first()
    )

    if destination is None:
        raise HTTPException(
            status_code=404,
            detail="Destination not found."
        )

    return destination


@router.get("/destinations/{destination_id}/features")
def get_destination_features(
    destination_id: int,
    db: Session = Depends(get_db)
):
    """
    Return the feature scores for a destination.
    """

    features = (
        db.query(DestinationFeature)
        .filter(
            DestinationFeature.destination_id == destination_id
        )
        .first()
    )

    if features is None:
        raise HTTPException(
            status_code=404,
            detail="Destination features not found."
        )

    return features


# ============================================================
# AUTHENTICATION
# ============================================================

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    """
    Register a new user.
    """

    normalized_email = user_data.email.lower()

    existing_user = (
        db.query(User)
        .filter(
            User.email == normalized_email
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    hashed_password = password_hash.hash(
        user_data.password
    )

    new_user = User(
        username=user_data.username,
        email=normalized_email,
        password_hash=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(
        new_user.user_id
    )

    return {
        "message": "User registered successfully",
        "access_token": token,
        "token_type": "bearer",
        "user_id": new_user.user_id,
        "username": new_user.username,
        "email": new_user.email,
    }


@router.post("/login")
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Authenticate an existing user.
    """

    normalized_email = user_data.email.lower()

    user = (
        db.query(User)
        .filter(
            User.email == normalized_email
        )
        .first()
    )

    invalid_credentials = HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )

    if user is None:
        raise invalid_credentials

    if not password_hash.verify(
        user_data.password,
        user.password_hash
    ):
        raise invalid_credentials

    token = create_access_token(
        user.user_id
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
    }


# ============================================================
# USER PREFERENCES
# ============================================================

@router.post("/preferences")
def save_preferences(
    preference: UserPreferenceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Save travel preferences for the currently
    authenticated user.
    """

    try:

        new_preference = UserPreference(
            user_id=current_user.user_id,
            budget=preference.budget,
            duration=preference.duration,
            climate=preference.climate,
            destination_type=preference.destination_type,
            season=preference.season,
        )

        db.add(new_preference)
        db.commit()
        db.refresh(new_preference)

        return {
            "message": "Preferences saved successfully",
            "data": {
                "preference_id": new_preference.preference_id,
                "user_id": new_preference.user_id,
                "budget": float(
                    new_preference.budget
                ),
                "duration": new_preference.duration,
                "climate": new_preference.climate,
                "destination_type": (
                    new_preference.destination_type
                ),
                "season": new_preference.season,
            }
        }

    except Exception as e:

        db.rollback()

        print(
            "ERROR SAVING PREFERENCES:"
        )
        print(repr(e))

        raise HTTPException(
            status_code=500,
            detail=(
                f"Could not save preferences: {str(e)}"
            )
        )


@router.get("/preferences")
def get_latest_preferences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Return the latest preferences of the
    authenticated user.
    """

    preference = (
        db.query(UserPreference)
        .filter(
            UserPreference.user_id
            == current_user.user_id
        )
        .order_by(
            UserPreference.preference_id.desc()
        )
        .first()
    )

    if preference is None:
        raise HTTPException(
            status_code=404,
            detail="User preferences not found."
        )

    return {
        "preference_id": preference.preference_id,
        "budget": float(preference.budget),
        "duration": preference.duration,
        "climate": preference.climate,
        "destination_type": (
            preference.destination_type
        ),
        "season": preference.season,
    }


@router.delete(
    "/user_preferences/{preference_id}"
)
def delete_preference(
    preference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Delete one preference belonging to
    the authenticated user.
    """

    preference = (
        db.query(UserPreference)
        .filter(
            UserPreference.preference_id
            == preference_id
        )
        .first()
    )

    if preference is None:
        raise HTTPException(
            status_code=404,
            detail="Preference not found."
        )

    if preference.user_id != current_user.user_id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to delete this preference."
        )

    db.delete(preference)
    db.commit()

    return {
        "message": "Preference deleted successfully."
    }


# ============================================================
# RECOMMENDATIONS
# ============================================================

@router.post("/recommend")
def recommend_destinations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Generate recommendations using the latest
    saved preferences of the authenticated user.
    """

    preference = (
        db.query(UserPreference)
        .filter(
            UserPreference.user_id
            == current_user.user_id
        )
        .order_by(
            UserPreference.preference_id.desc()
        )
        .first()
    )

    if preference is None:
        raise HTTPException(
            status_code=404,
            detail="User preferences not found."
        )

    destinations = (
        db.query(Destination)
        .all()
    )

    if not destinations:
        raise HTTPException(
            status_code=404,
            detail="No destinations found in the database."
        )

    try:

        recommendations = generate_recommendations(
            user_id=current_user.user_id,
            preference=preference,
            destinations=destinations,
            db=db,
        )

    except FileNotFoundError as e:

        raise HTTPException(
            status_code=503,
            detail=(
                "Recommendation model file not found: "
                f"{str(e)}"
            )
        )

    except Exception as e:

        print(
            "ERROR GENERATING RECOMMENDATIONS:"
        )
        print(repr(e))

        raise HTTPException(
            status_code=500,
            detail=(
                "Recommendation generation failed: "
                f"{str(e)}"
            )
        )

    if not recommendations:

        return {
            "message": "No matching destinations found.",
            "recommendations": []
        }

    return {
        "message": (
            "Recommendations generated successfully"
        ),
        "recommendations": recommendations,
    }


# ============================================================
# USER RECOMMENDATION HISTORY
# ============================================================

@router.get("/recommendations")
def get_user_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Return previous recommendations for
    the authenticated user.
    """

    return (
        db.query(Recommendation)
        .filter(
            Recommendation.user_id
            == current_user.user_id
        )
        .order_by(
            Recommendation.recommendation_id.desc()
        )
        .all()
    )


# ============================================================
# CONVERSATION HISTORY
# ============================================================

@router.post(
    "/conversations",
    status_code=status.HTTP_201_CREATED
)
def create_conversation(
    conversation_data: ConversationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new conversation for the
    authenticated user.
    """

    title = (
        conversation_data.title.strip()
        if conversation_data.title
        else "New trip chat"
    )

    if not title:
        title = "New trip chat"

    conversation = Conversation(
        user_id=current_user.user_id,
        title=title,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return {
        "conversation_id": (
            conversation.conversation_id
        ),
        "title": conversation.title,
        "created_at": conversation.created_at,
    }


@router.get("/conversations")
def get_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Return all conversations belonging to
    the authenticated user.
    """

    conversations = (
        db.query(Conversation)
        .filter(
            Conversation.user_id
            == current_user.user_id
        )
        .order_by(
            Conversation.created_at.desc()
        )
        .all()
    )

    return [
        {
            "conversation_id": (
                conversation.conversation_id
            ),
            "title": conversation.title,
            "created_at": conversation.created_at,
        }
        for conversation in conversations
    ]


@router.get("/conversations")
def get_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Return all conversations belonging to
    the authenticated user.
    """

    print("========== GET CONVERSATIONS ==========")
    print("Current user ID:", current_user.user_id)

    try:
        conversations = (
            db.query(Conversation)
            .filter(
                Conversation.user_id == current_user.user_id
            )
            .order_by(
                Conversation.created_at.desc()
            )
            .all()
        )

        print("Number of conversations:", len(conversations))

        result = [
            {
                "conversation_id": conversation.conversation_id,
                "title": conversation.title,
                "created_at": conversation.created_at,
            }
            for conversation in conversations
        ]

        print("Conversation result:", result)

        return result

    except Exception as e:
        print("========== CONVERSATION ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("========================================")

        raise HTTPException(
            status_code=500,
            detail=f"Conversation error: {type(e).__name__}: {str(e)}"
        )
    """
    Return one conversation and all its messages.

    The user can only access conversations
    belonging to their own account.
    """

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.conversation_id
            == conversation_id,
            Conversation.user_id
            == current_user.user_id,
        )
        .first()
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    messages = (
        db.query(ConversationMessage)
        .filter(
            ConversationMessage.conversation_id
            == conversation_id
        )
        .order_by(
            ConversationMessage.created_at.asc(),
            ConversationMessage.message_id.asc(),
        )
        .all()
    )

    return {
        "conversation_id": (
            conversation.conversation_id
        ),
        "title": conversation.title,
        "created_at": conversation.created_at,
        "messages": [
            {
                "message_id": message.message_id,
                "sender": message.sender,
                "message": message.message,
                "created_at": message.created_at,
            }
            for message in messages
        ],
    }


@router.post(
    "/conversations/{conversation_id}/messages",
    status_code=status.HTTP_201_CREATED
)
def save_conversation_message(
    conversation_id: int,
    message_data: ConversationMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Save a user or bot message to a conversation.
    """

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.conversation_id
            == conversation_id,
            Conversation.user_id
            == current_user.user_id,
        )
        .first()
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    message_text = message_data.message.strip()

    if not message_text:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    new_message = ConversationMessage(
        conversation_id=conversation_id,
        sender=message_data.sender,
        message=message_text,
    )

    db.add(new_message)

    # If this is the first user message, use it
    # as the conversation title.
    if message_data.sender == "user":

        existing_user_message = (
            db.query(ConversationMessage)
            .filter(
                ConversationMessage.conversation_id
                == conversation_id,
                ConversationMessage.sender
                == "user",
            )
            .first()
        )

        if existing_user_message is None:

            conversation.title = (
                message_text[:50]
            )

    db.commit()
    db.refresh(new_message)

    return {
        "message_id": new_message.message_id,
        "conversation_id": conversation_id,
        "sender": new_message.sender,
        "message": new_message.message,
        "created_at": new_message.created_at,
    }


@router.delete(
    "/conversations/{conversation_id}"
)
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Delete a conversation belonging to the
    authenticated user.

    Because ConversationMessage uses
    ON DELETE CASCADE, its messages are
    deleted as well.
    """

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.conversation_id
            == conversation_id,
            Conversation.user_id
            == current_user.user_id,
        )
        .first()
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    db.delete(conversation)
    db.commit()

    return {
        "message": "Conversation deleted successfully."
    }


# ============================================================
# CHATBOT
# ============================================================

@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Process a chatbot message.

    NOTE:
    Conversation history is handled by the
    /conversations endpoints above.
    """

    intent = detect_intent(
        request.message
    )

    # --------------------------------------------------------
    # Recommendation request
    # --------------------------------------------------------

    if intent == "recommendation":

        preference = (
            db.query(UserPreference)
            .filter(
                UserPreference.user_id
                == current_user.user_id
            )
            .order_by(
                UserPreference.preference_id.desc()
            )
            .first()
        )

        if preference is None:

            return {
                "intent": "recommendation",
                "response": (
                    "You're logged in, but I don't "
                    "have your travel preferences yet. "
                    "Let's get those now."
                ),
                "needs_login": False,
                "needs_preferences": True,
                "recommendations": None,
            }

        destinations = (
            db.query(Destination)
            .all()
        )

        if not destinations:

            return {
                "intent": "recommendation",
                "response": (
                    "I couldn't find any destinations "
                    "in the database."
                ),
                "needs_login": False,
                "needs_preferences": False,
                "recommendations": None,
            }

        try:

            recommendations = generate_recommendations(
                user_id=current_user.user_id,
                preference=preference,
                destinations=destinations,
                db=db,
            )

        except FileNotFoundError:

            return {
                "intent": "recommendation",
                "response": (
                    "The recommendation model isn't "
                    "ready yet. Please try again shortly."
                ),
                "needs_login": False,
                "needs_preferences": False,
                "recommendations": None,
            }

        except Exception as e:

            print(
                "CHAT RECOMMENDATION ERROR:"
            )
            print(repr(e))

            return {
                "intent": "recommendation",
                "response": (
                    "I encountered a problem while "
                    "generating your recommendations."
                ),
                "needs_login": False,
                "needs_preferences": False,
                "recommendations": None,
            }

        if not recommendations:

            return {
                "intent": "recommendation",
                "response": (
                    "I couldn't find strong matches "
                    "for your current preferences. "
                    "Try adjusting your budget, "
                    "climate, or trip type."
                ),
                "needs_login": False,
                "needs_preferences": False,
                "recommendations": [],
            }

        top_names = ", ".join(
            r["destination"]
            for r in recommendations[:3]
        )

        return {
            "intent": "recommendation",
            "response": (
                f"Based on your saved preferences, "
                f"you might love: {top_names}."
            ),
            "recommendations": recommendations,
            "needs_login": False,
            "needs_preferences": False,
        }

    # --------------------------------------------------------
    # Travel question
    # --------------------------------------------------------

    if intent == "travel_question":

        return {
            "intent": "travel_question",
            "response": (
                "This is a travel-related question."
            ),
            "recommendations": None,
            "needs_login": False,
            "needs_preferences": False,
        }

    # --------------------------------------------------------
    # Unrelated question
    # --------------------------------------------------------

    return {
        "intent": "unrelated",
        "response": (
            "I'm AfriGuide AI, a travel assistant "
            "focused on helping you discover and "
            "plan trips around Africa. Please ask "
            "me something related to African travel."
        ),
        "recommendations": None,
        "needs_login": False,
        "needs_preferences": False,
    }