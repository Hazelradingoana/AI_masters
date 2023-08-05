from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    user_email = Column(String(50), unique=True)
    password = Column(String(128))

# Create the SQLite database
engine = create_engine('sqlite:///user_accounts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_user(username,user_email, password):
    try:
        user = User( password=password,username=username,user_email=user_email)
        session.add(user)
        session.commit()
        print("User created successfully!")
    except IntegrityError:
        session.rollback()
        print("Email already exists. Please choose a different Email.")
