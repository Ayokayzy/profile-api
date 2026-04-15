from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="profile-api", version="1.0.0")


@app.get("/")
async def root():
    return JSONResponse(content={"message": "API is running"}, status_code=200)


@app.get("/health")
async def health():
    return JSONResponse(content={"message": "healthy"}, status_code=200)


@app.get("/me")
async def me():
    return JSONResponse(
        content={
            "name": "Ayokunle Ola-Akande",
            "email": "theayokayzy1@gmail.com",
            "github": "https://github.com/Ayokayzy/profile-api"
        },
        status_code=200
    )
