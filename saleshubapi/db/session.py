from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL_ASYNC = "postgresql+psycopg2://sa:12345678@db:5432/SalesHubDB"      

engine = create_engine(
    SQLALCHEMY_DATABASE_URL_ASYNC,
    pool_pre_ping = True
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine
)