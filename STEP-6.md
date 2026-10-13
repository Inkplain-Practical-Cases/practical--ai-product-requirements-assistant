# STEP 6 of 6 — Integrate and harden requirements

Install dependencies, run `python -m pytest -q`, and start `uvicorn app.main:app`. The full cumulative implementation provides tested local domain behavior and deterministic fixtures. The teaching code does **not** imply production approval, live services or all external adapters are complete. Audit the README limitations before deployment.

## Database (Entity) Relations
STEP-6 persists requirement intake and extraction-result metadata in SQLite. `requirement_analyses.requirement_id` is a foreign key to `requirement_requests.id`. The original brief and analysis text are not stored. Use `INKPLAIN_REQUIREMENTS_DB` to configure the database location. See `STEP-6.erd` and `STEP-6-ERD`.
