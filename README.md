# Profile API

A simple FastAPI-based profile service that provides user information via REST endpoints.

## Project Overview

This API returns profile information for Ayokunle Ola-Akande and includes health check endpoints.

## Endpoints

### `GET /`
Returns a confirmation message that the API is running.

**Response:**
```json
{
  "message": "API is running"
}
```

### `GET /health`
Returns the health status of the API.

**Response:**
```json
{
  "message": "healthy"
}
```

### `GET /me`
Returns the profile information of the user.

**Response:**
```json
{
  "name": "Ayokunle Ola-Akande",
  "email": "theayokayzy1@gmail.com",
  "github": "https://github.com/ayokayzy"
}
```

## Running Locally

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
5. Visit `http://localhost:8000` or `http://localhost:8000/docs` for the interactive Swagger UI

## Live Deployment

**Base URL:** `http://159.89.167.228`

- `http://159.89.167.228/` - API root
- `http://159.89.167.228/health` - Health check
- `http://159.89.167.228/me` - User profile

## Tech Stack

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
