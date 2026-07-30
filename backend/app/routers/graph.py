from fastapi import APIRouter

from app.services.graph_service import GraphService
from app.schemas import PaperCreate

router = APIRouter(
    prefix="/graph",
    tags=["Graph"]
)

service = GraphService()


@router.post("/paper")
def create_paper(
    paper: PaperCreate
):
    return service.create_paper(paper)


@router.get("/paper")
def get_papers():
    return service.get_papers()