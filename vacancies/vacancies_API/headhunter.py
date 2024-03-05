from requests import request

from vacancies.vacancies_API.search_API import SearchAPI
from vacancies.vacancy import Vacancy


class HeadhunterAPI(SearchAPI):
    def __init__(self):
        self._vacancies: list = list()
        self._params = {
            "page": 0,
            "text": "",
            "only_with_salary": 'true'
        }

    @property
    def vacancies(self):
        return self._vacancies

    def _pretty_view(self, data: list):
        vacancies = []
        for vacancy in data:
            if vacancy['salary']['from'] is None:
                continue
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

    def get_vacancies(self, search_request: str) -> list:
        self._params["text"] = search_request
        data = request(method="GET", url="https://api.hh.ru/vacancies/", params=self._params).json()['items']
        self._vacancies = self._pretty_view(data)
        return self._vacancies

    def get_top_n_vacancies(self, n: int, search_request: str) -> list:
        self._vacancies = self.get_vacancies(search_request)
        self._vacancies.sort(key=lambda x: x['salary_from'], reverse=True)
        return self._vacancies[:n]
