from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository


class UnitOfWork:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.users = UserRepository(db)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            await self.db.rollback()
        else:
            await self.db.commit()
