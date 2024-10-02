import logging
import time
from starlette.requests import Request
from starlette.responses import Response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pet.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("app-logger")

async def log_requests(request: Request, call_next):
    
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(f"Method: {request.method} URL: {request.url.path} "
                f"Status Code: {response.status_code} "
                f"Execution Time: {process_time:.4f} seconds")

    return response
