import uvicorn
from fastapi import FastAPI, APIRouter
from api.routes.security import security_route
from api.routes.users import users_route


app = FastAPI()
routes = APIRouter()


@app.get('/')
def welcome_page():
    return {'msg': 'Hi from backend!'}


routes.include_router(security_route, prefix='/security', tags=['security'])
routes.include_router(users_route)

app.include_router(routes)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
