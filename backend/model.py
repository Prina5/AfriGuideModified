from sqlalchemy import Integer, String, Column, Numeric, ForeignKey, Boolean, Float, Text, DateTime, CheckConstraint
from backend.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


## User Table(Model)
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime,
                        server_default=func.now(),
                        nullable=False)
    preferences = relationship(
        "UserPreference",
        back_populates="user",
        cascade="all, delete"
        )

    recommendations = relationship(
        "Recommendation",
        back_populates="user",
        cascade="all, delete"
        )


## Destination Table(Model)
class Destination(Base):
    __tablename__ = "destinations"
    destination_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    country = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    estimated_cost = Column(Numeric(15, 2), nullable=False)
    climate = Column(String(100), nullable=False)
    best_season = Column(String(120), nullable=False)
    latitude = Column(Numeric(10, 8), nullable=True)
    longitude = Column(Numeric(11, 8), nullable=True)
    image_url = Column(Text, nullable=True)

    features = relationship(
        "DestinationFeature",
        back_populates="destination",
        uselist=False,
        cascade="all, delete"
        )
    recommendations = relationship(
        "Recommendation",
        back_populates="destination"
        )


## Destination Features Table(Model)
class DestinationFeature(Base):
    __tablename__ = "destination_features"
    feature_id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey('destinations.destination_id', ondelete="CASCADE"),
                            unique=True,
                            nullable=False)
    destination_type = Column(String(255), nullable=False)
    wildlife_score = Column(Integer, nullable=False)
    adventure_score = Column(Integer, nullable=False)
    beach_score = Column(Integer, nullable=False)
    family_score = Column(Integer, nullable=False)
    history_score = Column(Integer, nullable=False)
    culture_score = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("wildlife_score BETWEEN 0 AND 5", name="check_wildlife_score"),
        CheckConstraint("adventure_score BETWEEN 0 AND 5", name="check_adventure_score"),
        CheckConstraint("beach_score BETWEEN 0 AND 5", name="check_beach_score"),
        CheckConstraint("family_score BETWEEN 0 AND 5", name="check_family_score"),
        CheckConstraint("history_score BETWEEN 0 AND 5", name="check_history_score"),
        CheckConstraint("culture_score BETWEEN 0 AND 5", name="check_culture_score"),
    )

    destination = relationship("Destination", back_populates="features")


## Preference table(Model) for any user
class UserPreference(Base):
    __tablename__ = "user_preferences"

    preference_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True)
    budget = Column(Numeric(15, 2), nullable=False)
    duration = Column(Integer, nullable=False)
    climate = Column(String(200), nullable=False)
    destination_type = Column(String(100), nullable=False)
    season = Column(String(50), nullable=True)

    __table_args__ = (
        CheckConstraint("budget >= 0", name="check_budget_positive"),
        CheckConstraint("duration > 0", name="check_duration_positive"),
    )

    user = relationship("User", back_populates="preferences")


## Recommendation(Model)
class Recommendation(Base):
    __tablename__ = "recommendations"
    recommendation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.destination_id", ondelete="CASCADE"), nullable=False)
    probability_score = Column(Numeric(10, 5), nullable=False)
    similarity_score = Column(Numeric(10, 5), nullable=False)
    recommended_at = Column(DateTime, server_default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("similarity_score BETWEEN 0 AND 1", name="check_similarity_score"),
        CheckConstraint("probability_score BETWEEN 0 AND 1", name="check_probability_score"),
    )

    user = relationship("User", back_populates="recommendations")
    destination = relationship("Destination", back_populates="recommendations")


class TrainingData(Base):
    __tablename__ = "training_data"

    training_id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.destination_id", ondelete="CASCADE"), nullable=False)

    budget = Column(Numeric(15, 2), nullable=False)
    duration = Column(Integer, nullable=False)

    climate = Column(String(100), nullable=False)
    destination_type = Column(String(100), nullable=False)

    wildlife_score = Column(Integer, nullable=False)
    adventure_score = Column(Integer, nullable=False)
    beach_score = Column(Integer, nullable=False)
    family_score = Column(Integer, nullable=False)
    history_score = Column(Integer, nullable=False)
    culture_score = Column(Integer, nullable=False)

    recommended = Column(Boolean, nullable=False)

    destination = relationship("Destination")

    __table_args__ = (
        CheckConstraint("budget >= 0", name="training_budget_positive"),
        CheckConstraint("duration > 0", name="training_duration_positive"),
        CheckConstraint("wildlife_score BETWEEN 0 AND 5", name="training_wildlife_score"),
        CheckConstraint("adventure_score BETWEEN 0 AND 5", name="training_adventure_score"),
        CheckConstraint("beach_score BETWEEN 0 AND 5", name="training_beach_score"),
        CheckConstraint("family_score BETWEEN 0 AND 5", name="training_family_score"),
        CheckConstraint("history_score BETWEEN 0 AND 5", name="training_history_score"),
        CheckConstraint("culture_score BETWEEN 0 AND 5", name="training_culture_score"),
    )
