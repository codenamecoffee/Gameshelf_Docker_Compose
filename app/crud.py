from sqlalchemy.orm import Session
from . import models, schemas


def get_games(db: Session):
    return db.query(models.Game).all()

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(title=game.title, status=game.status)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def update_game(db: Session, game_id: int, game: schemas.GameUpdate):
    db_game = get_game(db, game_id)
    if not db_game:
        return None
    if game.title is not None:
        db_game.title = game.title
    if game.status is not None:
        db_game.status = game.status
    db.commit()
    db.refresh(db_game)
    return db_game


def delete_game(db: Session, game_id: int):
    db_game = get_game(db, game_id)
    if not db_game:
        return None
    db.delete(db_game)
    db.commit()
    return db_game