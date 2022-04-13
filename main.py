import os
import time

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware

from src.api import security
from src.api.routes import users, equipments, parts, consumables

try:
    load_dotenv()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
except Exception as ex:
    print(f"Can't load dotenv: {ex}")
    host = '127.0.0.1'
    port = 8000
# finally:
#     origins = [f"http://{host}", f"http://{host}:{port}"]

routes = APIRouter()
app = FastAPI()


@app.get("/")
def welcome_page():
    return {'msg': 'Hi from backend!'}


routes.include_router(security.route, prefix='/security', tags=['Security'])
routes.include_router(users)
routes.include_router(equipments)
routes.include_router(parts)
routes.include_router(consumables)

app.include_router(routes)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

if __name__ == '__main__':
    uvicorn.run('main:app', host=host, port=port, reload=True, log_level="info")
