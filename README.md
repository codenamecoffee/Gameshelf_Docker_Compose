# 🎮 GameShelf

> Educational DevOps project developed during the professional training *School of Software Engineering* at Endava Uruguay — focused on containerization, orchestration, and backend development with FastAPI and PostgreSQL.

<br>

## 🧠 Overview

**GameShelf** is a web application for managing a collection of games. It provides full CRUD operations (Create, Read, Update, Delete) through a RESTful API, built with **FastAPI** and **SQLAlchemy**, and containerized using **Docker Compose**.

The project extends the concepts from *Movie Shop* (file-based persistence) by introducing a real **PostgreSQL database**, orchestrated together with the API in separate containers.

<br>

## Features
- Add, view, update, and delete games  
- Persistent storage using PostgreSQL  
- RESTful API built with FastAPI  
- Simple health check and `/docs` endpoint  
- Full Docker support (API + DB) 

<br>

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

<br>

## 🚀 Running the Application

### Prerequisites
- **Docker** (version 20.10+ recommended)
- **Docker Compose plugin** (usually included with Docker Desktop on Windows, or install separately on Linux)
- Python 3.8+ (optional, for manual local execution)

<br>

> **NOTE:** On most modern systems, use `docker compose` (without the hyphen).  
> On some Linux distributions, you may need to install the classic `docker-compose` tool and use it with the hyphen.

<br>

### ▶️ Run with Docker Compose (Recommended)

The preferred way to run **GameShelf** is using Docker Compose. This will start both the API and a PostgreSQL database.

1. Clone the repository:
   ```zsh
   git clone <repo-url>
   cd gameshelf
   ```

2. Start the application:

   * If you have the modern Docker Compose plugin (recommended):

   ```zsh
   docker compose up --build  // No hyphen
   ```

   * If you only have the classic tool:

   ```zsh
   docker-compose up --build  // With hyphen
   ```

3. Access the API:

- Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

- Base Endpoint: [http://localhost:8000](http://localhost:8000)

<br>

**NOTE**: When you run `docker compose up --build`, Docker will rebuild the image regardless of changes, which may result in unused images accumulating over time. You do not need to run `docker build` manually, but periodic cleanup with `docker image prune` is recommended.

---

#### Alternative: Local Development
If you prefer to run locally without Docker:

1. Install dependencies:
   ```zsh
   uv sync
   ```

2. Start a local PostgreSQL instance and set the `DATABASE_URL` environment variable.

3. Run the app:
   ```zsh
   uvicorn app.main:app --reload
   ```

4. Visit the same URLs.

<br>

## API Endpoints

| Method     | Endpoint      | Description                 |
| ---------- | ------------- | --------------------------- |
| **GET**    | `/games`      | List all games              |
| **GET**    | `/games/{id}` | Retrieve a single game      |
| **POST**   | `/games`      | Create a new game           |
| **PUT**    | `/games/{id}` | Update game title or status |
| **DELETE** | `/games/{id}` | Delete a game               |


All endpoints accept and return JSON unless otherwise noted. Example requests use `curl`.

<br>

### 1. List all games

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

<br>

### 2. Get a single game

**GET** `/games/{id}`
Returns details for a specific game.
```zsh
curl http://localhost:8000/games/1
```

Response:
```json
{"id": 1, "title": "Zelda", "status": "to_play"}
```

<br>

### 3. Create a game

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

<br>

### 4. Update a game

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

<br>

### 5. Delete a game

**DELETE** `/games/{id}`
Deletes a game entry.
```zsh
curl -X DELETE http://localhost:8000/games/1
```

Response:
```json
{"id": 1, "title": "Zelda", "status": "to_play"}
```

<br>

### 6. Health & Docs

- **GET** `/` redirects to `/docs` (minimal HTML docs)
- **GET** `/docs` serves a simple HTML documentation page

<br>

## Testing
Run unit tests with:
```zsh
pytest
```

<br>

## Docker & Compose Details

The docker-compose.yml file defines two services:

- **db**: PostgreSQL container with a persistent volume.

- **api**: FastAPI app container built from the provided Dockerfile.

<br>

## High Availability for the Database

The database container is configured with a restart policy (`restart: always`) to maximize its availability. This ensures the database service automatically restarts in case of failure, minimizing downtime and making API testing and development more reliable.

<br>

## 👥 Authors

- **Federico González** ([codenamecoffee](https://github.com/codenamecoffee))
- **Mariana Guerra** ([MarianaGuerraC](https://github.com/MarianaGuerraC))

<br>

## License
This project is licensed under the MIT License.


