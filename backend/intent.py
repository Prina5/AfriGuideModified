def detect_intent(message: str) -> str:

    message = message.lower().strip()

    recommendation_keywords = [
        "recommend",
        "recommendation",
        "suggest",
        "where should i go",
        "where can i go",
        "best destination",
        "destination for me",
        "trip for me",
        "place to visit"
    ]

    travel_keywords = [
        "travel",
        "visit",
        "tourist",
        "destination",
        "wildlife",
        "safari",
        "hotel",
        "beach",
        "climate",
        "weather",
        "visa",
        "flight",
        "tour"
    ]

    if any(keyword in message for keyword in recommendation_keywords):
        return "recommendation"

    if any(keyword in message for keyword in travel_keywords):
        return "travel_question"

    return "unrelated"
