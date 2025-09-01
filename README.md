# ACEestFitness — DevOps Assignment

Small Flask fitness tracker used for a DevOps assignment.
Features: add workouts (name, duration, reps, calories), view table, reset all workouts. In-memory storage.

---

## What this repo contains
- `aceest_fitness/` — Python package (Flask app)
  - `app.py` — Flask application
  - `__init__.py`
  - `templates/` — HTML templates
- `tests/` — pytest unit tests
- `Dockerfile` — containerization
- `.github/workflows/main.yml` — CI pipeline (GitHub Actions)
- `requirements.txt`, `pytest.ini`, `.pre-commit-config.yaml`
- `.gitignore`

---

## Prerequisites (local)
- Python 3.10+ (3.12 used during dev)
- pip
- Docker (for container run)
- (optional) `pre-commit`

---

## Run locally (development)
```bash
# create and activate virtualenv (recommended)
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
python -m aceest_fitness.app
# open http://127.0.0.1:5000
