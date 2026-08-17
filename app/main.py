from fastapi import FastAPI

app = FastAPI(
    title="CloudOps API",
    version="1.0.1"
)


@app.get("/")
def root():
    return {
        "application": "CloudOps",
        "status": "running",
        "version": "1.0.1"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }