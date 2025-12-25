from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, user: User) -> User:
        self.db.add(user)
        return user