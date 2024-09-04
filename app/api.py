from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from service_1c.statuses import statuses
from service_1c.tamplates import (
    MessageTemplate,
    flyers_template
)

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
    orders = await statuses.order_response(telefon=telefon.telefon)
    for order in orders['data']['orders']:
        message = MessageTemplate(order=order).message()
        data.append(message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": data
        }
    )


@router.post("/user_flyers/")
async def get_user_flyers(telefon: APICreateRequest) -> JSONResponse:
    flyer = await statuses.flyer_response(telefon=telefon.telefon)
    message = flyers_template(flyer=flyer)
    return JSONResponse(
        content={
            "status": "ok",
            "data": message
        }
    )
