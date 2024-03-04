from abc import ABC, abstractmethod

from vacancies.vacancy import Vacancy


class SearchAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_request: str) -> list:
        pass

    def _pretty_view(self, data: list):
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(
                position=vacancy['name'],
                url=vacancy['url'],
                salary_from=vacancy['salary']['from'],
                salary_to=vacancy['salary']['to'],
                description=vacancy['snippet']['responsibility'],
                must_know=vacancy['snippet']['requirement']
            ).__dict__)
        self._vacancies = vacancies
        return self._vacancies
