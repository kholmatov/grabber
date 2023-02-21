import logging
from fastapi import FastAPI
from app.spiders.aptoide import Aptoide
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()


@app.get('/get/url')
async def get(url: str) -> JSONResponse:
    aptoide = Aptoide()
    content, status = await aptoide.get(url)
    json_compatible_item_data = jsonable_encoder(content)
    return JSONResponse(content=json_compatible_item_data,
                        status_code=status)
