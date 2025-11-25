from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from views import book

app = FastAPI(
    title="My FastAPI App",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(book.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)