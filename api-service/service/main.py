"""Microservice main module."""

import os

import dotenv
import uvicorn
from app.routers import records
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

__all__ = []

dotenv.load_dotenv()


app = FastAPI(root_path='')
app.include_router(records.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/ping')
async def check_service_alive() -> JSONResponse:
    """Return ping-pong response.

    Returns: JSONResponse

    """
    return JSONResponse(
        content='Service is alive'
    )


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True,
        host=os.getenv('APP_HOST'),
        port=int(os.getenv('APP_PORT'))
    )
