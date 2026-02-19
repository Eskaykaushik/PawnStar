from fastapi import FastAPI

app = FastAPI(title="PawnStar API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "pawnstar",
        "message": "PawnStar backend is running"
    } 