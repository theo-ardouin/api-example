from abc import ABC, abstractmethod
from app.entities import Uri


class ICatApi(ABC):
    @abstractmethod
    def get(self) -> Uri:
        pass
