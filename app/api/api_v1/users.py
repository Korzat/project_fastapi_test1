from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.unit_of_work import UnitOfWork
from app.repositories.user_repository import UserRepository
from app.db.session import get_session
from app.schemas.users import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter()



@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate,session: AsyncSession = Depends(get_session)):
    async with UnitOfWork(session) as uow:
        user = await UserService().register(uow, data.name, data.email)
        return user