# AfriGuide AI — Backend

## Setup

```bash

python -m venv .venv
#windows: .venv\Scripts\activate

pip install -r requirements.txt


```

## Run order

```bash
python test_db.py                 # confirm Postgres connectivity
python create_tables.py           # create tables
python seed_data.py               # seed destinations + features
python generate_training_data.py  # generate synthetic training_data rows
python train_model.py             # train + save the recommendation model to backend/models/
uvicorn app:app --reload          # start the API
```

## What changed 

- **Auth**: `/login` and `/register` now issue a JWT. Every route that touches
  a user's data (`/preferences`, `/recommend`, `/recommendations`,
  `DELETE /user_preferences/{id}`) requires `Authorization: Bearer <token>`
  and derives the user from the token — never from a client-supplied
  `user_id`. Send the token from `/register` or `/login` on those requests.
- `requirements.txt` re-saved as UTF-8 (was UTF-16LE) and now includes
  `pwdlib`, `email-validator`, and `PyJWT`, which the code already
  depended on but weren't listed.
- `config.py` validates required env vars up front with a clear error
  
  not the current working directory, and loaded lazily so a missing
  model returns a clean `503` instead of crashing the whole API on boot.
- Removed a dead duplicate `/` route.
- Added CORS middleware (configurable via `CORS_ORIGINS` in `.env`).
  
