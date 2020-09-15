from order import Order
from order_status import OrderStatus
class Action():
    def __init__(self, live_orders):
        self.live_orders = live_orders

    @staticmethod
    def place_order(instrument, order_type,limit_price):
        order = Order(instrument, order_type, limit_price)
        return order

    @staticmethod
    def cancel_order(orders):
        for order in orders:
            if order.status == 'active':
                order.status = 'canceled'

