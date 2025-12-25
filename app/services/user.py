from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.db.unit_of_work import UnitOfWork
from app.models.users import User


class UserService:
    async def register(self, uow: UnitOfWork, name: str, email: str) -> User:
        user = User(name=name, email=email)
        await uow.users.add(user)
        return user