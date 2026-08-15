## Imports
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sqlalchemy import create_engine

from backend.config import DATABASE_URL, MODELS_DIR

engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM training_data", engine)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

## Encoding columns
climate_encoder = LabelEncoder()
df["climate"] = climate_encoder.fit_transform(df["climate"])

type_encoder = LabelEncoder()
df["destination_type"] = type_encoder.fit_transform(df["destination_type"])

## Input features
X = df[
    [
        "budget",
        "duration",
        "climate",
        "destination_type",
        "wildlife_score",
        "adventure_score",
        "beach_score",
        "family_score",
        "history_score",
        "culture_score",
    ]
]

## Target
y = df["recommended"]

## Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

## Training the Random Forest
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced",
)

model.fit(X_train, y_train)

## Making predictions
predictions = model.predict(X_test)

## Evaluate model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1 Score:", f1_score(y_test, predictions))

## Detailed report
print(classification_report(y_test, predictions))

## Confusion matrix
print(confusion_matrix(y_test, predictions))

## Save trained model + encoders (always to backend/models, regardless of cwd)
os.makedirs(MODELS_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODELS_DIR, "recommendation_model.pkl"))
joblib.dump(climate_encoder, os.path.join(MODELS_DIR, "climate_encoder.pkl"))
joblib.dump(type_encoder, os.path.join(MODELS_DIR, "type_encoder.pkl"))

print(f"Model and encoders saved to {MODELS_DIR}")
