from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.graph import router as graph_router

app = FastAPI(
    title="Knowledge Graph API"
)

app.include_router(health_router)
app.include_router(graph_router)