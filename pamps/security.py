"""Boiler Plate"""
from passlib.context import CryptContext
from pamps.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
    return pwd_context.hash(password)

class HashedPassword(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("String Required")
        
        hashed_password = get_password_hash(v)
        return cls(hashed_password)
