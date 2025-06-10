# Run loop: tick → signal → order → fill → update

class BacktestEngine:
    def __init__(self, strategy, data_handler, broker):
        self.strategy = strategy
        self.data_handler = data_handler
        self.broker = broker

    def run(self):
        self.strategy.on_start()
        while True:
            bar = self.data_handler.get_next()
            if bar is None:
                break
            orders = self.strategy.on_data(bar)
            self.broker.execute_orders(orders, bar['close'])
        self.strategy.on_end()
