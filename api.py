from fastapi import APIRouter
from .endpoints import consulta_peddos

api_router = APIRouter()
api_router.include_router(consulta_peddos.router, prefix="/v2/pedidos", tags=["pedidos"])


