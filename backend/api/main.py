from fastapi import FastAPI
from .routers import router as routes
import firebase_admin
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

default_app = firebase_admin.initialize_app()

app.include_router(routes)

