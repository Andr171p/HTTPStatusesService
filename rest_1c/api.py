from rest_1c.server.http_session import HTTPSession
from rest_1c.settings.parameters import RequestData, RequestHeaders
from rest_1c import models
from rest_1c.utils import extract_orders_data

from misc.format_data import format_telefon


class StatusAPI(HTTPSession):
    request_headers = RequestHeaders()
    request_data = RequestData()

    async def order_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.order}',
            'telefon': f'{telefon}'
        }
        data = models.OrderModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def orders_response(self):
        data = {
            'command': f'{self.request_data.orders}',
            'active': 'true'
        }
        data = models.OrdersModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        result = extract_orders_data(response=response)
        return result

    async def flyer_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.flyer}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = models.FlyerModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response

    async def history_response(self, telefon: str):
        telefon = format_telefon(telefon=telefon)
        data = {
            'command': f'{self.request_data.history}',
            'telefon': f'{telefon}',
            'project': f'{self.request_headers.project}'
        }
        data = models.HistoryModel.model_validate(data)
        response = await self.post_request(data=data.model_dump())
        return response


status_api = StatusAPI()


import asyncio


f = asyncio.run(status_api.flyer_response("89829764729"))
print(f)