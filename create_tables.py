from backend.database import engine, Base
import backend.model  # noqa: F401  (registers models with Base.metadata)

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables successfully created")
