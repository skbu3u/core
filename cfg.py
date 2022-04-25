import os

from dotenv import load_dotenv

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
