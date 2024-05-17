import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI
from classy_fastapi import Routable, get


@asynccontextmanager
async def lifespan(app: FastAPI):
    # https://fastapi.tiangolo.com/advanced/events/#lifespan
    yield


class DefaultRouter(Routable):
    @get("/")
    def index():
        return "Hello World"


def main():
    app = FastAPI(lifespan=lifespan)
    default_router = DefaultRouter()

    app.include_router(default_router.router)
    return app


if __name__ == "__main__":
    example_app = main()
    uvicorn.run(example_app, host="localhost", port=8000)
