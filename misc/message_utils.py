from misc.tamplates import MessageTemplate


def order_to_message(order: dict) -> dict:
    template = MessageTemplate(order=order)
    message = template.message()
    return message

