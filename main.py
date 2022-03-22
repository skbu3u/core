import uvicorn
from fastapi import FastAPI, APIRouter
from api.routes import security, users, equipments, parts


app = FastAPI()
routes = APIRouter()


@app.get('/')
def welcome_page():
    return {'msg': 'Hi from backend!'}


routes.include_router(security.route, prefix='/security', tags=['Security'])
routes.include_router(users.route)
routes.include_router(equipments.route)
routes.include_router(parts.route)

app.include_router(routes)


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
