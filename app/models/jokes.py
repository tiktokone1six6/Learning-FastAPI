from sqlalchemy import Column, Integer, String
from ..database import Base

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    setup = Column(String, index=True)
    punchline = Column(String, index=True)