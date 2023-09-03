from saleshubapi.db.session import AsyncSessionLocal

async def get_async_db():
    async with AsyncSessionLocal as db:
        yield db
        await db.commit()