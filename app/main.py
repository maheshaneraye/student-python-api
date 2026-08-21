from fastapi import FastAPI

app = FastAPI(
    title="Student Python API",
    version="1.0.0",
    description="Sample Python FastAPI microservice for CI/CD demonstration"
)

@app.get("/")
def read_root():
    return {
        "service": "student-python-api",
        "status": "online",
        "message": "Welcome to Student Python API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": "2026-08-21T00:00:00Z"
    }

@app.get("/api/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}!",
        "version": "1.0.0"
    }
