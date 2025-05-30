from sqlalchemy import create_engine

from .models.task import Base

DB_URI = "mysql+pymysql://root@database:3306/main?charset=utf8"

engine = create_engine(DB_URI, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    reset_database()