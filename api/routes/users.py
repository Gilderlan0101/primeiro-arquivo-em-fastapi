from fastapi import APIRouter


''' Router: receber uma rota padrão antes de mostra a proxima rota, ex
    /user/ <-- rota inicial
    /user/teste <-- rota teste '''
router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not fold"}},
)

# Criando rotas
@router.get("/")
async def home():
    return {'stautus': 'ok'}