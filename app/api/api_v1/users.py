from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.crud.users_crud import add_user
from app.db.session import get_session
from app.schemas.users import UserCreate, UserResponse

router = APIRouter(prefix="/users")



@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate,session: AsyncSession = Depends(get_session)):
    try:
        user = await add_user(session, data.name, data.email)
        await session.commit()
        await session.refresh(user)
        return user
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )