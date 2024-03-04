import os

from dotenv import load_dotenv

from file_editor.file_helper import FileHelper
from vacancies.vacancy import Vacancy

load_dotenv()
VACANCIES_DATA_PATH = os.getenv("VACANCIES_DATA_PATH")


class JsonHelper:

    @staticmethod
    def add_vacancy(vacancies: list[Vacancy]) -> None:
        data: list = FileHelper.read_file(VACANCIES_DATA_PATH)
        FileHelper.save_data(VACANCIES_DATA_PATH, data + vacancies)

    @staticmethod
    def get_vacancies_by_salary(salary_from: int, salary_to: int) -> list:
        result: list = list()
        vacancies = FileHelper.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if salary_from <= vacancy["salary_from"] <= salary_to:
                result.append(vacancy)
        return result

    @staticmethod
    def delete_vacancy(vacancies: list[Vacancy]) -> None:
        data: list = FileHelper.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if vacancy in data:
                data.remove(vacancy)
        FileHelper.save_data(VACANCIES_DATA_PATH, data)
