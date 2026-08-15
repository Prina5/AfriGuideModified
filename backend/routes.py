from fastapi import APIRouter, Depends, HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from backend.auth import create_access_token, get_current_user
from backend.database import get_db
from backend.intent import detect_intent
from backend.model import (
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
    UserLogin,
    UserPreferenceCreate,
    UserRegister,
)

password_hash = PasswordHash.recommended()
router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to AfriGuide AI"}


# --------------------------------------------------
# Destinations (public, read-only)
# --------------------------------------------------

@router.get("/destinations")
def get_destinations(db: Session = Depends(get_db)):
    """Return all destinations."""
    return db.query(Destination).all()


@router.get("/destinations/{destination_id}")
def get_destination(destination_id: int, db: Session = Depends(get_db)):
    destination = (
        db.query(Destination)
        .filter(Destination.destination_id == destination_id)
        .first()
    )
    if destination is None:
        raise HTTPException(status_code=404, detail="Destination Not Found.")
    return destination


@router.get("/destinations/{destination_id}/features")
def get_destination_features(destination_id: int, db: Session = Depends(get_db)):
    features = (
        db.query(DestinationFeature)
        .filter(DestinationFeature.destination_id == destination_id)
        .first()
    )
    if features is None:
        raise HTTPException(status_code=404, detail="Destination feature not found")
    return features


# --------------------------------------------------
# Auth
# --------------------------------------------------

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    normalized_email = user_data.email.lower()

    existing_user = db.query(User).filter(User.email == normalized_email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = password_hash.hash(user_data.password)

    new_user = User(
        username=user_data.username,
        email=normalized_email,
        password_hash=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(new_user.user_id)

    return {
        "message": "User registered successfully",
        "access_token": token,
        "token_type": "bearer",
        "user_id": new_user.user_id,
        "username": new_user.username,
        "email": new_user.email,
    }


@router.post("/login")
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    normalized_email = user_data.email.lower()

    user = db.query(User).filter(User.email == normalized_email).first()

    # Same error for "no such user" and "wrong password" so we don't
    # leak which emails are registered.
    invalid_credentials = HTTPException(status_code=401, detail="Invalid email or password")

    if user is None:
        raise invalid_credentials

    if not password_hash.verify(user_data.password, user.password_hash):
        raise invalid_credentials

    token = create_access_token(user.user_id)

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
    }


# --------------------------------------------------
# Preferences (require auth; always scoped to the caller)
# --------------------------------------------------

@router.post("/preferences")
def save_preferences(
    preference: UserPreferenceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_preference = UserPreference(
        user_id=current_user.user_id,
        **preference.model_dump(),
    )
    db.add(new_preference)
    db.commit()
    db.refresh(new_preference)
    return {
        "message": "Preferences saved successfully",
        "data": new_preference,
    }


@router.delete("/user_preferences/{preference_id}")
def delete_preference(
    preference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    preference = (
        db.query(UserPreference)
        .filter(UserPreference.preference_id == preference_id)
        .first()
    )
    if preference is None:
        raise HTTPException(status_code=404, detail="Preference Not Found")

    if preference.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this preference")

    db.delete(preference)
    db.commit()
    return {"message": "Preference deleted successfully."}


# --------------------------------------------------
# Recommendations (require auth; always scoped to the caller)
# --------------------------------------------------

@router.post("/recommend")
def recommend_destinations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Generate recommendations for the authenticated user."""
    preference = (
        db.query(UserPreference)
        .filter(UserPreference.user_id == current_user.user_id)
        .order_by(UserPreference.preference_id.desc())
        .first()
    )

    if preference is None:
        raise HTTPException(status_code=404, detail="User preferences not found.")

    destinations = db.query(Destination).all()

    try:
        recommendations = generate_recommendations(
            user_id=current_user.user_id,
            preference=preference,
            destinations=destinations,
            db=db,
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))

    return {
        "message": "Recommendations generated successfully",
        "recommendations": recommendations,
    }


@router.get("/recommendations")
def get_user_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Recommendation)
        .filter(Recommendation.user_id == current_user.user_id)
        .all()
    )


# --------------------------------------------------
# Chat
# --------------------------------------------------

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    intent = detect_intent(request.message)

    if intent == "recommendation":
        return {
            "intent": "recommendation",
            "response": "This request will be processed by the recommendation system.",
        }

    if intent == "travel_question":
        return {
            "intent": "travel_question",
            "response": "This is a travel-related question.",
        }

    return {
        "intent": "unrelated",
        "response": (
            "I'm AfriGuide AI, a travel assistant focused on "
            "helping you discover and plan trips around Africa. "
            "Please ask me something related to African travel."
        ),
    }
