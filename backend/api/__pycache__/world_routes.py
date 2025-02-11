from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from backend.services import world_manager

router = APIRouter()

class WorldGenParams(BaseModel):
    theme: str = Field(..., description="The theme of the world (e.g., Fantasy, Sci-Fi, Post-Apocalyptic)", example="Fantasy")
    character_name: str = Field(..., description="The protagonist's name", example="Skromdar")
    character_description: str = Field(
        default="A mysterious hero",
        description="Brief description of the protagonist",
        example="A holy Orc paladin."
    )

@router.get("/generate_world/")
def generate_world(params: WorldGenParams = Depends()):
    world_history = world_manager.generate_world_history(params.theme, params.character_name, params.character_description)
    return {"world_history": world_history}