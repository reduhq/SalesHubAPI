from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

SQLALCHEMY_DATABASE_URL_ASYNC = "postgresql+asyncpg://sa:12345678@db:5432/SalesHubDB"      

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL_ASYNC
)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)