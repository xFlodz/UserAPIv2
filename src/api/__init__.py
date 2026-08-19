from fastapi import APIRouter

from src.api.users import router as user_router

router = APIRouter()

router.include_router(user_router, tags=['user'], prefix='/api/user')


__all__ = ['router']


