from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, SessionLocal
from fastapi.responses import HTMLResponse, RedirectResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GameShelf", docs_url=None, redoc_url=None)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def simple_docs():
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>GameShelf – API Docs</title>
      <style>
        body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Helvetica,Arial,sans-serif;margin:2rem;line-height:1.6;color:#1b1f24}
        code{background:#f4f6f8;padding:.15rem .35rem;border-radius:.35rem}
        pre{background:#f4f6f8;padding:1rem;border-radius:.5rem;overflow:auto}
        h1{margin-top:0}
        .ep{border-left:4px solid #d0d7de;padding:.5rem 1rem;margin:1rem 0}
        .method{font-weight:700;padding:.15rem .5rem;border-radius:.35rem;margin-right:.5rem}
        .GET{background:#e7f5ff}
        .POST{background:#e6fcf5}
        .PUT{background:#fff4e6}
        .DELETE{background:#fff0f6}
      </style>
    </head>
    <body>
      <h1>GameShelf – Minimal API Docs</h1>
      <p>Small, dependency-free docs page listing available endpoints.</p>

      <div class="ep"><span class="method GET">GET</span><code>/games</code>
        <div>List all games.</div>
        <pre>curl http://localhost:8000/games</pre>
      </div>

      <div class="ep"><span class="method GET">GET</span><code>/games/{id}</code>
        <div>Get a single game.</div>
        <pre>curl http://localhost:8000/games/1</pre>
      </div>

      <div class="ep"><span class="method POST">POST</span><code>/games</code>
        <div>Create a game.</div>
        <pre>curl -X POST http://localhost:8000/games \\
  -H 'Content-Type: application/json' \\
  -d '{"title":"Zelda","status":"to_play"}'</pre>
      </div>

      <div class="ep"><span class="method PUT">PUT</span><code>/games/{id}</code>
        <div>Update a game title or status (<code>to_play</code> | <code>playing</code> | <code>finished</code>).</div>
        <pre>curl -X PUT http://localhost:8000/games/1 \\
  -H 'Content-Type: application/json' \\
  -d '{"status":"playing"}'</pre>
      </div>

      <div class="ep"><span class="method DELETE">DELETE</span><code>/games/{id}</code>
        <div>Delete a game.</div>
        <pre>curl -X DELETE http://localhost:8000/games/1</pre>
      </div>

      <p>Health: <code>GET /</code> redirects here.</p>
    </body>
    </html>
    """


@app.post("/games", response_model=schemas.GameOut)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db, game)


@app.get("/games", response_model=list[schemas.GameOut])
def list_games(db: Session = Depends(get_db)):
    return crud.get_games(db)


@app.get("/games/{game_id}", response_model=schemas.GameOut)
def get_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game(db, game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@app.put("/games/{game_id}", response_model=schemas.GameOut)
def update_game(game_id: int, game: schemas.GameUpdate, db: Session = Depends(get_db)):
    db_game = crud.update_game(db, game_id, game)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@app.delete("/games/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.delete_game(db, game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"ok": True}