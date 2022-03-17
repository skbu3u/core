import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.routes import users, security

app = FastAPI()
route = APIRouter()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'msg': 'Hello World'}


route.include_router(users.users_route, prefix='/users', tags=['users'])
route.include_router(security.security_route, prefix='/security', tags=['security'])

app.include_router(route)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
