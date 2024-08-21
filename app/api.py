from fastapi import FastAPI

from service_1c.statuses import Statuses
from service_1c.tamplates import MessageTemplate

from app.settings import EndPoints, JsonResult


app = FastAPI()


@app.post(EndPoints.order)
async def order_api(telefon: str):
    statuses = Statuses()
    order = await statuses.order_response(telefon=telefon)
    message = MessageTemplate(order=order).message()
    return JsonResult(message=message).order_json
