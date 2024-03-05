import os

from dotenv import load_dotenv
from requests import request

from vacancies.vacancies_API.search_API import SearchAPI
from vacancies.vacancy import Vacancy

load_dotenv()
API_KEY = os.getenv("SUPER_JOB_API_KEY")


class SuperJobAPI(SearchAPI):
    """
    A class for searching and retrieving job vacancies from SuperJob API.
    """

    def __init__(self):
        """
        Initialize the SuperJob API object with an empty list of vacancies and default search parameters.
        """
        self._vacancies: list = list()
        self._params: dict = {
            'keywords': ''
        }
        self._headers: dict = {
            'X-Api-App-Id': API_KEY
        }

    @property
    def vacancies(self):
        """
        A property for getting the list of vacancies retrieved from SuperJob API.

        Returns:
            list: A list of vacancies retrieved from SuperJob API.
        """
        return self._vacancies

    def _pretty_view(self, data: list) -> list:
        """
        A private method for processing the raw data retrieved from SuperJob API and creating a list of
        Vacancy objects.

        Args:
            data (list): A list of raw data retrieved from SuperJob API.

        Returns:
            list: A list of Vacancy objects created from the raw data.
        """
        vacancies = []
        for vacancy in data:
            if vacancy['payment_from'] == 0 or vacancy['payment_from'] is None:
                continue
            vacancies.append(Vacancy(
                position=vacancy['profession'],
                url=vacancy['link'],
                salary_from=vacancy['payment_from'],
                salary_to=vacancy['payment_to'],
                description=vacancy['vacancyRichText'],
                must_know=vacancy['candidat']
            ).__dict__)
        self._vacancies = vacancies
        return self._vacancies

    def get_vacancies(self, search_request: str) -> list:
        """
        A method for searching and retrieving job vacancies from SuperJob API based on a search query.

        Args:
            search_request (str): The search query used for searching job vacancies.

        Returns:
            list: A list of job vacancies retrieved from SuperJob API based on the search query.
        """
        self._params['keywords'] = search_request
        data = request(method="GET", url='https://api.superjob.ru/2.0/vacancies/', params=self._params,
                       headers=self._headers).json()['objects']
        self._vacancies = self._pretty_view(data)
        return self._vacancies

    def get_top_n_vacancies(self, n: int, search_request: str) -> list:
        """
        A method for retrieving the top n job vacancies based on salary from SuperJob API based on a search query.

        Args:
            n (int): The number of top job vacancies to retrieve.
            search_request (str): The search query used for searching job vacancies.

        Returns:
            list: A list of the top n job vacancies based on salary retrieved from SuperJob API
            based on the search query.
        """
        self._vacancies = self.get_vacancies(search_request)
        self._vacancies.sort(key=lambda x: x['salary_from'], reverse=True)
        return self._vacancies[:n]
