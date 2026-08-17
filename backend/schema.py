from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional


# ============================================================
# AUTHENTICATION
# ============================================================

class UserRegister(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        description="Minimum 8 characters"
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ============================================================
# USER PREFERENCES
# ============================================================

class UserPreferenceCreate(BaseModel):
    budget: float = Field(
        gt=0,
        description=(
            "Travel budget must be greater than zero "
            "and does not include the trip from home country"
        )
    )

    duration: int = Field(
        gt=0,
        description="Trip duration must be greater than zero"
    )

    climate: Literal[
        "Tropical",
        "Coastal",
        "Desert",
        "Temperate"
    ]

    destination_type: Literal[
        "Wildlife",
        "Beach",
        "Historical",
        "Adventure",
        "Cultural"
    ]

    season: Optional[str] = None


# ============================================================
# CHATBOT
# ============================================================

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        description="User's message"
    )


class ChatResponse(BaseModel):
    intent: str
    response: str

    recommendations: Optional[list[dict]] = None

    needs_login: bool = False
    needs_preferences: bool = False


# ============================================================
# CONVERSATIONS
# ============================================================

class ConversationCreate(BaseModel):
    title: Optional[str] = None


class ConversationMessageCreate(BaseModel):
    sender: Literal[
        "user",
        "bot"
    ]

    message: str = Field(
        min_length=1,
        description="Conversation message"
    )