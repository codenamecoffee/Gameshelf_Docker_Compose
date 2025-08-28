from pydantic import BaseModel
from enum import Enum

class GameStatus(str, Enum):
    to_play = "to_play"
    playing = "playing"
    finished = "finished"

class GameBase(BaseModel):
    title: str
    status: GameStatus = GameStatus.to_play

class GameCreate(GameBase):
    pass

class GameUpdate(BaseModel):
    title: str | None = None
    status: GameStatus | None = None

class GameOut(GameBase):
    id: int
    class Config:
        orm_mode = True