from abc import ABC, abstractmethod


class SearchAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_request: str) -> list:
        pass

    @abstractmethod
    def _pretty_view(self, data: list):
        pass
