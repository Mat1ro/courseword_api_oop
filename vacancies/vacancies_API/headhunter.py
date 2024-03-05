from requests import request

from vacancies.vacancies_API.search_API import SearchAPI
from vacancies.vacancy import Vacancy


class HeadhunterAPI(SearchAPI):
    """
    A class for searching and retrieving job vacancies from HeadHunter API.
    """

    def __init__(self):
        """
        Initialize the HeadhunterAPI object with an empty list of vacancies and default search parameters.
        """
        self._vacancies: list = list()
        self._params = {
            "page": 0,
            "text": "",
            "only_with_salary": 'true'
        }

    @property
    def vacancies(self):
        """
        A property for getting the list of vacancies retrieved from HeadHunter API.

        Returns:
            list: A list of vacancies retrieved from HeadHunter API.
        """
        return self._vacancies

    def _pretty_view(self, data: list):
        """
        A private method for processing the raw data retrieved from HeadHunter API and creating a list of
        Vacancy objects.

        Args:
            data (list): A list of raw data retrieved from HeadHunter API.

        Returns:
            list: A list of Vacancy objects created from the raw data.
        """
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
        """
        A method for searching and retrieving job vacancies from HeadHunter API based on a search query.

        Args:
            search_request (str): The search query used for searching job vacancies.

        Returns:
            list: A list of job vacancies retrieved from HeadHunter API based on the search query.
        """
        self._params["text"] = search_request
        data = request(method="GET", url="https://api.hh.ru/vacancies/", params=self._params).json()['items']
        self._vacancies = self._pretty_view(data)
        return self._vacancies

    def get_top_n_vacancies(self, n: int, search_request: str) -> list:
        """
        A method for retrieving the top n job vacancies based on salary from HeadHunter API based on a search query.

        Args:
            n (int): The number of top job vacancies to retrieve.
            search_request (str): The search query used for searching job vacancies.

        Returns:
            list: A list of the top n job vacancies based on salary retrieved from HeadHunter API
            based on the search query.
        """
        self._vacancies = self.get_vacancies(search_request)
        self._vacancies.sort(key=lambda x: x['salary_from'], reverse=True)
        return self._vacancies[:n]
