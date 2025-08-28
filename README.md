
# GameShelf

GameShelf is a web application for managing a collection of games. It provides CRUD operations for games, allowing users to add, view, update, and delete game entries. The backend is built with FastAPI and uses SQLAlchemy for database interactions.

## Features
- Add new games to your shelf
- View all games
- Update game details
- Delete games
- RESTful API endpoints

## Project Structure
```
├── app/
│   ├── crud.py         # CRUD operations for games
│   ├── database.py     # Database connection and setup
│   ├── main.py         # FastAPI application entry point
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas for request/response
├── tests/
│   └── test_games.py   # Unit tests for game functionality
├── Dockerfile          # Docker configuration for the app
├── docker-compose.yml  # Docker Compose setup
├── pyproject.toml      # Project dependencies and settings
```

## Getting Started

### Prerequisites
- Docker (recommended)
- Python 3.8+ (for local development)

### Running the Application (Recommended)

The preferred way to run GameShelf is using Docker Compose. This will start both the API and a PostgreSQL database.

1. Clone the repository:
   ```zsh
   git clone <repo-url>
   cd gameshelf
   ```
2. Start the application:
   ```zsh
   docker-compose up --build
   ```
3. The API will be available at [http://localhost:8000](http://localhost:8000)

#### Alternative: Local Development
If you prefer to run locally without Docker:
1. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   # or
   poetry install
   ```
2. Start a local PostgreSQL instance and set the `DATABASE_URL` environment variable.
3. Run the app:
   ```zsh
   uvicorn app.main:app --reload
   ```

## API Endpoints

All endpoints accept and return JSON unless otherwise noted. Example requests use `curl`.

### List all games
**GET** `/games`
Returns a list of all games.
```zsh
curl http://localhost:8000/games
```
Response:
```json
[
  {"id": 1, "title": "Zelda", "status": "to_play"},
  {"id": 2, "title": "Mario", "status": "playing"}
]
```

### Get a single game
**GET** `/games/{id}`
Returns details for a specific game.
```zsh
curl http://localhost:8000/games/1
```
Response:
```json
{"id": 1, "title": "Zelda", "status": "to_play"}
```

### Create a game
**POST** `/games`
Creates a new game entry.
```zsh
curl -X POST http://localhost:8000/games \
  -H 'Content-Type: application/json' \
  -d '{"title":"Zelda","status":"to_play"}'
```
Response:
```json
{"id": 1, "title": "Zelda", "status": "to_play"}
```

### Update a game
**PUT** `/games/{id}`
Updates the title or status of a game. Status must be one of: `to_play`, `playing`, `finished`.
```zsh
curl -X PUT http://localhost:8000/games/1 \
  -H 'Content-Type: application/json' \
  -d '{"status":"playing"}'
```
Response:
```json
{"id": 1, "title": "Zelda", "status": "playing"}
```

### Delete a game
**DELETE** `/games/{id}`
Deletes a game entry.
```zsh
curl -X DELETE http://localhost:8000/games/1
```
Response:
```json
{"id": 1, "title": "Zelda", "status": "to_play"}
```

### Health & Docs
- **GET** `/` redirects to `/docs` (minimal HTML docs)
- **GET** `/docs` serves a simple HTML documentation page

## Testing
Run unit tests with:
```zsh
pytest
```

## License
This project is licensed under the MIT License.
