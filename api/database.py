from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URI = "mysql+aiomysql://root@database:3306/main?charset=utf8"

async_engine  = create_async_engine(ASYNC_DB_URI, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

Base = declarative_base()

async def get_database():
    async with async_session() as session:
        yield session