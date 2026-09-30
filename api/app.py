from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="OptiForge",
    description="Self-Healing and Autonomous IT Operations API",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root() -> dict:
    return {
        "name": "OptiForge",
        "message": "Self-Healing IT Operations System",
        "status": "running",
    }