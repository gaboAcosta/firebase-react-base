from fastapi import FastAPI
from .router import base_router
from dotenv import load_dotenv
import firebase_admin

load_dotenv()

app = FastAPI()

app.include_router(base_router)

default_app = firebase_admin.initialize_app()