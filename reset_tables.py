from backend.database import Base, engine
import backend.model                      

confirm = input(
    "This will DROP ALL TABLES and delete all data. Type 'yes' to continue: "
)

if confirm.strip().lower() == "yes":
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped.")
else:
    print("Cancelled. No changes made.")