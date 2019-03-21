from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    @abstractmethod
    def handling_score(self, command: dict):
        return float

    @abstractmethod
    def handle(self):
        return
