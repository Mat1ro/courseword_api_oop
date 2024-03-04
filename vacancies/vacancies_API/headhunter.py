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

    def get_vacancies(self, search_request: str) -> list:
        self.params["text"] = search_request
        data = request(method="GET", url="https://api.hh.ru/vacancies/", params=self.params).json()["items"]
        return data
