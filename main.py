import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src.api import security
from src.api.routes import users, equipments, parts, consumables

load_dotenv()
host = os.getenv('HOST')
port = int(os.getenv('PORT'))
routes = APIRouter()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def welcome_page():
    return {'msg': 'Hi from backend!'}


routes.include_router(security.route, prefix='/security', tags=['Security'])
routes.include_router(users)
routes.include_router(equipments)
routes.include_router(parts)
routes.include_router(consumables)

app.include_router(routes)


if __name__ == '__main__':
    uvicorn.run('main:app', host=host, port=port, reload=True, log_level="info")
