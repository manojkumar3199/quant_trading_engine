# Order types and handling

from enum import Enum

class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"

class Order:
    def __init__(self, symbol, quantity, order_type=OrderType.MARKET, price=None, stop_price=None, side='BUY'):
        self.symbol = symbol
        self.quantity = quantity
        self.order_type = order_type
        self.price = price
        self.stop_price = stop_price
        self.side = side
        self.filled = False
        self.fill_price = None
