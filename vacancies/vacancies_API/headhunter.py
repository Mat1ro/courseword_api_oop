from requests import request

from vacancies.vacancies_API.search_API import SearchAPI


class HeadhunterAPI(SearchAPI):
    def __init__(self):
        self._vacancies: list = list()
        self.params = {
            "page": 0,
            "text": "",
            "only_with_salary": 'true'
        }

    @property
    def vacancies(self):
        return self._vacancies

    def get_vacancies(self, search_request: str) -> list:
        self.params["text"] = search_request
        data = request(method="GET", url="https://api.hh.ru/vacancies/", params=self.params).json()["items"]
        self._vacancies = self._pretty_view(data)
        return self._vacancies
