from fastapi import APIRouter
from fastapi.responses import JSONResponse

from rest_1c.api import status_api

from misc.message_utils import order_to_message
from misc.tamplates import flyers_template

from app.schemas import APICreateRequest


router = APIRouter()


@router.get("/")
async def get_hello_world() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "ok",
            "data": "Hello world!"
        },
    )


@router.post("/user_orders/")
async def get_user_order(telefon: APICreateRequest) -> JSONResponse:
    data = []
    orders = await status_api.order_response(telefon=telefon.telefon)
    messages = map(order_to_message, orders['data']['orders'])
    for message in messages:
        data.append(message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": data
        }
    )


@router.post("/user_flyers/")
async def get_user_flyers(telefon: APICreateRequest) -> JSONResponse:
    flyer = await status_api.flyer_response(telefon=telefon.telefon)
    message = flyers_template(flyer=flyer['data'])
    return JSONResponse(
        content={
            "status": "ok",
            "data": message
        }
    )
