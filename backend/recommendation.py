import os

import joblib

from backend.config import MODELS_DIR
from backend.model import Recommendation
from backend.preprocess import prepare_features
from backend.utils import normalize_probability, recommendation_message

_model = None


def _load_model():
    global _model
    if _model is not None:
        return _model

    model_path = os.path.join(MODELS_DIR, "recommendation_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            "Recommendation model not found. "
            "Run `python train_model.py` first to train and save the model."
        )

    _model = joblib.load(model_path)
    return _model


def generate_recommendations(user_id, preference, destinations, db):
    model = _load_model()

    results = []
    new_recommendations = []

    for destination in destinations:
        # Skip destinations that were never assigned a feature row
        # (would otherwise raise AttributeError on destination.features)
        if destination.features is None:
            continue

        X = prepare_features(preference, destination)
        probability = model.predict_proba(X)[0][1]

        new_recommendations.append(
            Recommendation(
                user_id=user_id,
                destination_id=destination.destination_id,
                probability_score=float(probability),
                similarity_score=float(probability),
            )
        )

        results.append({
            "destination": destination.name,
            "country": destination.country,
            "probability": normalize_probability(probability),
            "message": recommendation_message(probability)
        })

    try:
        db.add_all(new_recommendations)
        db.commit()
    except Exception:
        db.rollback()
        raise

    results.sort(key=lambda x: x["probability"], reverse=True)

    return results[:5]
