import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.testclient import TestClient
from starlette.middleware.cors import CORSMiddleware

from cfg import host, port, origins
from src.api.routes.base import users, equipments, parts, consumables, tasks
from src.api.routes.search import search
from src.api.routes.security import security

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])


@app.get("/")
def welcome_page():
    return {'msg': 'Hi from backend!'}


main_router = APIRouter()
main_router.include_router(users)
main_router.include_router(equipments)
main_router.include_router(parts)
main_router.include_router(consumables)
main_router.include_router(tasks)
main_router.include_router(search, prefix='/search', tags=['Search'])
main_router.include_router(security, prefix='/security', tags=['Security'])

app.include_router(main_router)
client = TestClient(app)

if __name__ == '__main__':
    uvicorn.run('main:app',
                host=host,
                port=port,
                reload=True,
                timeout_keep_alive=0,
                log_level="info",
                use_colors=True)
