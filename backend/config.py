import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BACKEND_DIR)
MODELS_DIR = os.path.join(BACKEND_DIR, "models")


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            f"Set it in your .env file (see .env.example)."
        )
    return value


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DB_HOST = _require_env("DB_HOST")
DB_PORT = _require_env("DB_PORT")
DB_NAME = _require_env("DB_NAME")
DB_USER = _require_env("DB_USER")

# Encode special characters like @, :, /
DB_PASSWORD = quote_plus(_require_env("DB_PASSWORD"))

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

# Log raw SQL only when explicitly enabled (keep off in production)
DB_ECHO = os.getenv("DB_ECHO", "false").lower() == "true"

# --------------------------------------------------
# AUTH
# --------------------------------------------------
JWT_SECRET_KEY = _require_env("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# --------------------------------------------------
# CORS
# --------------------------------------------------
# Comma-separated list of allowed origins, e.g. "http://localhost:3000,https://afriguide.app"
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]
