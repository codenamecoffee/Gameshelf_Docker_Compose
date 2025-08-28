from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from .database import Base
import enum

class GameStatus(str, enum.Enum):
    to_play = "to_play"
    playing = "playing"
    finished = "finished"

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(Enum(GameStatus), nullable=False, default=GameStatus.to_play)
    created_at = Column(TIMESTAMP, server_default=func.now())
