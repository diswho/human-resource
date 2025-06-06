from fastapi import APIRouter

from app.api.routes import items, login, users, utils, attendance, employee, income

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(employee.router, prefix="/employee", tags=["employee"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["attendance"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(income.router, prefix="/income", tags=["income"])
