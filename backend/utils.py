def normalize_probability(probability):
    """
    Convert a probability into a percentage.
    """
    return round(probability * 100, 2)


## Recommendation helper function
def recommendation_message(probability):

    if probability >= 0.90:
        return "Excellent match"

    elif probability >= 0.75:
        return "Very good match"

    elif probability >= 0.60:
        return "Good match"

    return "Possible match"
