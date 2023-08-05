from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))

# Create the SQLite database
engine = create_engine('sqlite:///user_accounts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
