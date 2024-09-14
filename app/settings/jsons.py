class JsonResult:
    def __init__(self, message) -> None:
        self.order_json = {'order': f'{message}'}
        self.flyers_json = {'flyers': f'{message}'}