# Student Python FastAPI App (CI Demo)

A simple, lightweight FastAPI REST microservice ready for automated CI testing and Docker Hub deployment.

## Features
* **Framework:** FastAPI (Python 3.11)
* **Automated Testing:** Pytest + HTTPX
* **Container:** Production-ready `python:3.11-slim` Dockerfile with health checks
* **CI Workflow:** GitHub Actions (`.github/workflows/ci.yml`)

---

## Local Development

```bash
# 1. Create and activate virtualenv
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run unit tests
pytest -v

# 4. Start local server
uvicorn app.main:app --reload --port 8000
```

---

## Pushing to Your GitHub Repository

```bash
# Inside sample-projects/python-fastapi-app directory
git init
git add .
git commit -m "feat: initial python fastapi app with CI pipeline"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
```

### Required GitHub Secrets
In your GitHub Repo: `Settings` ➔ `Secrets and variables` ➔ `Actions`
* `DOCKERHUB_USERNAME`: Your Docker Hub username
* `DOCKERHUB_TOKEN`: Your Docker Hub Personal Access Token (PAT)

automation test -1 

