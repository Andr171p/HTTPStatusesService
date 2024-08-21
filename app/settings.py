class EndPoints:
    order = "/order"
    flyers = "/flyers"


class JsonResult:
    def __init__(self, message):
        self.order_json = {'order': f'{message}'}
        self.flyers_json = {'flyers': f'{message}'}


class ServerConsts:
    pass
