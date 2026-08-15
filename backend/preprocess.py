import os

import joblib
import pandas as pd

from backend.config import MODELS_DIR

_climate_encoder = None
_type_encoder = None


def _load_encoders():
    """
    Lazily loads the encoders on first use instead of at import time,
    so the whole API doesn't crash on startup if the model hasn't been
    trained yet -- only the /recommend route fails, with a clear error.
    """
    global _climate_encoder, _type_encoder

    if _climate_encoder is not None and _type_encoder is not None:
        return _climate_encoder, _type_encoder

    climate_path = os.path.join(MODELS_DIR, "climate_encoder.pkl")
    type_path = os.path.join(MODELS_DIR, "type_encoder.pkl")

    if not os.path.exists(climate_path) or not os.path.exists(type_path):
        raise FileNotFoundError(
            "Recommendation model encoders not found. "
            "Run `python train_model.py` first to train and save the model."
        )

    _climate_encoder = joblib.load(climate_path)
    _type_encoder = joblib.load(type_path)
    return _climate_encoder, _type_encoder


def prepare_features(preference, destination):
    """
    Combine user preferences and destination features into
    a single feature vector.
    """
    climate_encoder, type_encoder = _load_encoders()

    try:
        climate = climate_encoder.transform([preference.climate])[0]
    except ValueError:
        raise ValueError("Unsupported climate value")

    try:
        destination_type = type_encoder.transform([destination.features.destination_type])[0]
    except ValueError:
        raise ValueError("Unsupported destination type")

    features = {
        "budget": float(preference.budget),
        "duration": preference.duration,
        "climate": climate,
        "destination_type": destination_type,
        "wildlife_score": destination.features.wildlife_score,
        "adventure_score": destination.features.adventure_score,
        "beach_score": destination.features.beach_score,
        "family_score": destination.features.family_score,
        "history_score": destination.features.history_score,
        "culture_score": destination.features.culture_score,
    }

    return pd.DataFrame([features])
