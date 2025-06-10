# Position tracking, cash, PnL

class Portfolio:
    def __init__(self, starting_cash):
        self.cash = starting_cash
        self.positions = {}
        self.history = []

    def update_fill(self, order):
        """
        Updates position and cash based on filled order.
        """
        pass  # TODO
