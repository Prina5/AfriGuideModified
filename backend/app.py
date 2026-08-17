from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import model  # noqa: F401  (import needed so create_all sees all tables)
from backend.database import Base, engine
from backend.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AfriGuide AI API",
    description="Backend API for the AfriGuide AI tourist Recommendation system",
    version="1.0.0",
)

# ✅ Enable CORS so your frontend can reach the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now allow all origins; later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router)
