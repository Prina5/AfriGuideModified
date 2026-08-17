




import re
import uuid

CLIMATE_OPTIONS = ["Tropical", "Coastal", "Desert", "Temperate"]
TYPE_OPTIONS = ["Wildlife", "Beach", "Historical", "Adventure", "Cultural"]

TYPE_SYNONYMS = {
    "safari": "Wildlife", "wildlife": "Wildlife", "animals": "Wildlife",
    "beach": "Beach", "coast": "Beach", "sea": "Beach",
    "history": "Historical", "historical": "Historical", "heritage": "Historical",
    "adventure": "Adventure", "adrenaline": "Adventure", "hiking": "Adventure",
    "culture": "Cultural", "cultural": "Cultural",
}
CLIMATE_SYNONYMS = {
    "tropical": "Tropical", "humid": "Tropical",
    "coastal": "Coastal",
    "desert": "Desert", "dry": "Desert", "hot": "Desert",
    "temperate": "Temperate", "mild": "Temperate",
}

WELCOME_MESSAGE = (
    "Welcome to AfriGuide AI! Today we're going to have a short conversation "
    "to learn about your travel preferences, so I can recommend the best "
    "destination for you. Let's see where you should go next.\n\n"
    
)


QUESTIONS = [
    ("budget", "What's your travel budget in USD? (e.g. 1500)"),
    ("duration", "How many days are you planning to travel?"),
    ("climate", "What climate do you prefer: Tropical, Coastal, Desert, or Temperate?"),
    ("destination_type", "What kind of trip: Wildlife, Beach, Historical, Adventure, or Cultural?"),
    ("wildlife_score", "On a scale of 0-5, how much do you care about seeing wildlife?"),
    ("adventure_score", "On a scale of 0-5, how important is adventure/activity?"),
    ("beach_score", "On a scale of 0-5, how much do you want beach time?"),
    ("family_score", "On a scale of 0-5, how family-friendly should it be?"),
    ("history_score", "On a scale of 0-5, how much do you care about historical sites?"),
    ("culture_score", "On a scale of 0-5, how important is cultural immersion?"),
]

# In-memory store. Fine for dev / a single server process.
# Swap for Redis if you ever run multiple workers/instances.
_sessions = {}


def start_session():
    session_id = str(uuid.uuid4())
    # step = -1 means "greeting not sent yet"
    _sessions[session_id] = {"answers": {}, "step": -1}
    return session_id


def _extract_number(text):
    match = re.search(r"\d+(\.\d+)?", text)
    return float(match.group()) if match else None


def _match_option(text, options, synonyms):
    text_lower = text.lower()
    for option in options:
        if option.lower() in text_lower:
            return option
    for keyword, option in synonyms.items():
        if keyword in text_lower:
            return option
    return None


def process_message(session_id, message):
    """
    Returns: (session_id, response_text_or_None, done, answers_or_None)
    - If not done: response_text is the greeting (first turn) or the next question.
    - If done: answers_or_None is the fully collected dict of 10 fields.
    """
    session = _sessions.get(session_id)
    if session is None:
        session_id = start_session()
        session = _sessions[session_id]

    step = session["step"]

    # step -1: this is the user's very first message ("hi", etc.) — nothing to
    # parse yet. Send the welcome message + first question together, then
    # advance straight to expecting an answer to question 0 (budget).
    if step == -1:
        session["step"] = 1  # next message will be treated as the answer to QUESTIONS[0]
        return session_id, WELCOME_MESSAGE, False, None

    if step > 0:
        field, question_text = QUESTIONS[step - 1]
        value = None

        if field == "budget":
            value = _extract_number(message)
        elif field == "duration":
            num = _extract_number(message)
            value = int(num) if num is not None else None
        elif field == "climate":
            value = _match_option(message, CLIMATE_OPTIONS, CLIMATE_SYNONYMS)
        elif field == "destination_type":
            value = _match_option(message, TYPE_OPTIONS, TYPE_SYNONYMS)
        elif field.endswith("_score"):
            num = _extract_number(message)
            if num is not None and 0 <= num <= 5:
                value = int(num)

        if value is None:
            return session_id, f"Sorry, I didn't catch that. {question_text}", False, None

        session["answers"][field] = value

    if session["step"] >= len(QUESTIONS):
        return session_id, None, True, session["answers"]

    _, question_text = QUESTIONS[session["step"]]
    session["step"] += 1
    return session_id, question_text, False, None


def reset_session(session_id):
    _sessions.pop(session_id, None)