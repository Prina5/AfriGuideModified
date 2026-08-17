from backend.database import engine, Base
from backend.model import (
    User,
    Destination,
    DestinationFeature,
    UserPreference,
    Recommendation,
    TrainingData,
    Conversation,
    ConversationMessage
)


print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Tables successfully created")