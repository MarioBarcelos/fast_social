from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import create_engine
from pamps.settings import settings

engine = create_engine(
    settings.get("default_db.uri"),
    connect_args=settings.get("default_db.connect_args", {}),
    echo=settings.get("default_db.echo", False),
)

def get_session():
    with Session(engine) as session:
        yield session

ActiveSession = Depends(get_session)