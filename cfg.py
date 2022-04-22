import os

from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

try:
    load_dotenv()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
except Exception as ex:
    print(f"Can't load dotenv: {ex}")
    host = '127.0.0.1'
    port = 8000
finally:
    origins = ["*"]  # [f"http://{host}", f"http://{host}:{port}"]

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"])
    main_router = APIRouter()
    additional_router = APIRouter()
