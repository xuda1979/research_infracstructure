from order_status import OrderStatus

class Order():
    def __init__(self, instrument, order_type, limit_price, quantity, side, order_id):
        self.instrument = instrument
        self.order_type = order_type
        self.limit_price = limit_price
        self.quantity = quantity
        self.side = side,
        self.order_id = order_id
        self.remaining_quantity = quantity
        self.status = 'live'





