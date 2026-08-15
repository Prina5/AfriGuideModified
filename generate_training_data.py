import random

from backend.database import SessionLocal
from backend.model import Destination, DestinationFeature, TrainingData

db = SessionLocal()

try:
    # --------------------------------------------------
    # LOAD DESTINATIONS
    # --------------------------------------------------
    destinations = db.query(Destination).join(DestinationFeature).all()

    if not destinations:
        raise RuntimeError(
            "No destinations with features found."
        )

    # --------------------------------------------------
    # POSSIBLE USER PREFERENCES
    # --------------------------------------------------
    climates = ["Tropical", "Coastal", "Desert", "Temperate"]
    types = ["Wildlife", "Beach", "Historical", "Adventure", "Cultural"]

    # --------------------------------------------------
    # GENERATE TRAINING DATA
    # --------------------------------------------------
    training_records = []

    for _ in range(10000):
        destination = random.choice(destinations)

        # USER PREFERENCES
        budget = random.randint(300, 3000)
        duration = random.randint(2, 14)
        climate = random.choice(climates)
        destination_type = random.choice(types)
        wildlife_preference = random.randint(0, 5)
        adventure_preference = random.randint(0, 5)
        beach_preference = random.randint(0, 5)
        family_preference = random.randint(0, 5)
        history_preference = random.randint(0, 5)
        culture_preference = random.randint(0, 5)

        # DESTINATION CHARACTERISTICS
        wildlife = destination.features.wildlife_score
        adventure = destination.features.adventure_score
        beach = destination.features.beach_score
        family = destination.features.family_score
        history = destination.features.history_score
        culture = destination.features.culture_score

        # CALCULATE RECOMMENDATION SCORE
        score = 0

        if budget >= float(destination.estimated_cost):
            score += 1
        if climate == destination.climate:
            score += 1
        if destination_type == destination.features.destination_type:
            score += 1
        if wildlife_preference >= wildlife:
            score += 1
        if adventure_preference >= adventure:
            score += 1
        if beach_preference >= beach:
            score += 1
        if family_preference >= family:
            score += 1
        if history_preference >= history:
            score += 1
        if culture_preference >= culture:
            score += 1

        # FINAL LABEL
        recommended = score >= 6

        record = TrainingData(
            destination_id=destination.destination_id,
            budget=budget,
            duration=duration,
            climate=climate,
            destination_type=destination_type,
            wildlife_score=wildlife_preference,
            adventure_score=adventure_preference,
            beach_score=beach_preference,
            family_score=family_preference,
            history_score=history_preference,
            culture_score=culture_preference,
            recommended=recommended,
        )

        training_records.append(record)

    # --------------------------------------------------
    # SAVE TO DATABASE
    # --------------------------------------------------
    db.add_all(training_records)
    db.commit()

    print("Training data generated successfully!")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()
