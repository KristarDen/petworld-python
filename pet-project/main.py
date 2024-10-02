from contextlib import asynccontextmanager
from core.models import db_helper
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from api import router as api_router
from core.utils.logger import log_requests


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.middleware("http")(log_requests)

main_app.include_router(
    api_router,
)
