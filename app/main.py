
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="TaskFlow API",
    description="A smart task management platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to TaskFlow!",
        "status": "Application is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
