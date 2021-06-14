from sqlalchemy import Column, String, Boolean, Integer
from src.config.database import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'<User(id="{self.id}", email={self.email})>'
