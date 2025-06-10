# Fill models, slippage

class ExecutionModel:
    def __init__(self, slippage=0.0, commission=0.0):
        self.slippage = slippage
        self.commission = commission

    def fill_order(self, order, market_price):
        """
        Simulate order fill and apply slippage/commission.
        """
        order.filled = True
        order.fill_price = market_price * (1 + self.slippage)
        return order
