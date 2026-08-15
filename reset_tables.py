
from backend.database import Base, engine
import backend.model                      # noqa: F401  (registers models with Base.metadata)

confirm = input(
   
)

if confirm.strip().lower() == "yes":
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped.")
else:
    print("Cancelled. No changes made.")