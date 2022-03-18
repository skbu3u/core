import uvicorn
from fastapi import FastAPI, APIRouter
from api.routes import security

app = FastAPI()
route = APIRouter()


@app.get('/')
def home():
    return {'msg': 'Hi from backend'}


route.include_router(security.security_route, prefix='/security', tags=['security'])

app.include_router(route)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
