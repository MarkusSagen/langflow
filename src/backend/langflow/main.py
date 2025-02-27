from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langflow.api.endpoints import router as endpoints_router
from langflow.api.validate import router as validate_router


def create_app():
    """Create the FastAPI app and include the router."""
    server = FastAPI()

    origins = [
        "*",
    ]

    server.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.include_router(endpoints_router)
    server.include_router(validate_router)
    return server


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=7860)
