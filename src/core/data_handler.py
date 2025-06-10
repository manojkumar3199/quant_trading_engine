# Market data loading & streaming

class DataHandler:
    """
    Loads and feeds historical or live data into the engine.
    """
    def __init__(self, data_source):
        self.data_source = data_source
        self.current_bar = None

    def get_next(self):
        """
        Returns next tick or bar of data.
        """
        raise NotImplementedError("Override this method in subclass")
