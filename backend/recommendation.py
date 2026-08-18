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

    model_path = os.path.join(
        MODELS_DIR,
        "recommendation_model.pkl"
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            "Recommendation model not found. "
            "Run `python train_model.py` first to train and save the model."
        )

    _model = joblib.load(model_path)

    return _model


def generate_recommendations(
    user_id,
    preference,
    destinations,
    db
):
    """
    Generate destination recommendations for a user.

    Budget is treated as a HARD constraint:

    1. Find the cheapest destination in the database.
    2. If the user's budget is below that amount,
       do not run the ML model.
    3. Only pass destinations the user can afford
       to the ML model.
    4. The ML model ranks the affordable destinations
       according to the user's other preferences.
    """

  

    user_budget = float(
        preference.budget
    )


    destination_costs = [
        float(destination.estimated_cost)
        for destination in destinations
        if destination.estimated_cost is not None
    ]

    if not destination_costs:

        raise ValueError(
            "No destination estimated costs are available."
        )

    minimum_budget = min(
        destination_costs
    )


   
    #
    # Example:
    #
    # Cheapest destination = $500
    # User budget = $300
    #
    # Do NOT allow the ML model to make a recommendation.


    if user_budget < minimum_budget:

        return {
            "budget_too_low": True,
            "minimum_budget": minimum_budget,
            "recommendations": []
        }


   

    model = _load_model()


    results = []

    new_recommendations = []


 

    for destination in destinations:

        # Skip destinations without feature data
     

        if destination.features is None:
            continue


   
        #
        # A destination costing more than the user's budget
        # must NEVER be recommended, regardless of how high
        # the ML probability is.
       

        destination_cost = float(
            destination.estimated_cost
        )

        if destination_cost > user_budget:
            continue


        # Prepare features for the ML model
       

        X = prepare_features(
            preference,
            destination
        )


        # Get model probability
      

        probability = model.predict_proba(
            X
        )[0][1]

        # Save recommendation to database
        

        new_recommendations.append(
            Recommendation(
                user_id=user_id,
                destination_id=destination.destination_id,
                probability_score=float(
                    probability
                ),
                similarity_score=float(
                    probability
                ),
            )
        )


        # Prepare response for frontend
       

        results.append(
            {
                "destination": destination.name,

                "country": destination.country,

                "probability": normalize_probability(
                    probability
                ),

                "message": recommendation_message(
                    probability
                )
            }
        )


    # NO AFFORDABLE DESTINATIONS
  
    #
    # This can happen if:
    #
    # minimum_budget <= user_budget
    #
    # but, for example, the only destinations with feature
    # rows cost more than the user's budget.
   

    if not results:

        return {
            "budget_too_low": False,
            "minimum_budget": minimum_budget,
            "recommendations": []
        }



    try:

        db.add_all(
            new_recommendations
        )

        db.commit()

    except Exception:

        db.rollback()

        raise


   

    results.sort(
        key=lambda x: x["probability"],
        reverse=True
    )



    return {
        "budget_too_low": False,
        "minimum_budget": minimum_budget,
        "recommendations": results[:5]
    }