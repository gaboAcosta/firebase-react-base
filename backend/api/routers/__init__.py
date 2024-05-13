from fastapi import APIRouter
from .users_router import router as users_router
from .auth_router import router as auth_router

router = APIRouter(
    prefix="/api/v1",
    responses={404: {"description": "Not found"}},
)

router.include_router(users_router)
router.include_router(auth_router)
