from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    email: EmailStr
    hashed_password: str


class UserOut(UserIn):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
