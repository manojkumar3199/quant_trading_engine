# Order simulation or routing

class Broker:
    def __init__(self, portfolio, execution_model):
        self.portfolio = portfolio
        self.execution_model = execution_model

    def execute_orders(self, orders, market_price):
        for order in orders:
            filled_order = self.execution_model.fill_order(order, market_price)
            self.portfolio.update_fill(filled_order)
