 # Abstract base class

from abc import ABC, abstractmethod

class StrategyBase(ABC):
    """
    Abstract base class for all strategies.
    """

    @abstractmethod
    def on_data(self, data: dict):
        """
        Called on every new market data update.
        Should return a list of Order objects.
        """
        pass

    def on_start(self):
        """Optional: Called once at strategy start."""
        pass

    def on_end(self):
        """Optional: Called once at strategy end."""
        pass
