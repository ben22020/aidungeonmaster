from fastapi import FastAPI
from backend.api.world_routes import router as world_router
from backend.api.npc_routes import router as npc_router


app = FastAPI()


app.include_router(world_router)
app.include_router(npc_router)
@app.get("/")
def home():
    """Default API landing page."""
    return {"message": "Welcome to AI Dungeon Master API!"}