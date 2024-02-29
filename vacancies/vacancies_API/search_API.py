from abc import ABC, abstractmethod


class SearchAPI(ABC):
    @abstractmethod
    def get_vacancies(self, position: str) -> list:
        pass
