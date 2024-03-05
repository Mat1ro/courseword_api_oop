import os

from dotenv import load_dotenv

from file_editor.file_helper import FileHelper

load_dotenv()
VACANCIES_DATA_PATH = os.getenv("VACANCIES_DATA_PATH")


class JsonHelper:
    """
    A class for working with vacancies in JSON format.
    """

    @staticmethod
    def add_vacancy(vacancies: list[dict]) -> None:
        """
        Adds new vacancies to the file.

        Args:
        vacancies (list[dict]): A list of vacancies to add.

        Returns:
        None

        Notes:
        The data is read from the file, new vacancies are added to the list, and then the data is saved to the file.
        """
        data: list = FileHelper.read_file(VACANCIES_DATA_PATH)
        FileHelper.save_data(VACANCIES_DATA_PATH, data + vacancies)

    @staticmethod
    def get_vacancies_by_salary(salary_from: int, salary_to: int) -> list:
        """
        Returns a list of vacancies whose salary is in the specified range.

        Args:
        salary_from (int): The lower limit of the salary range.
        salary_to (int): The upper limit of the salary range.

        Returns:
        list: A list of vacancies whose salary is in the specified range.

        Notes:
        The data is read from the file and vacancies whose salary is in the specified range are searched.
        """
        result: list = list()
        vacancies = FileHelper.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if salary_from <= vacancy["salary_from"] <= salary_to:
                result.append(vacancy)
        return result

    @staticmethod
    def delete_vacancy(vacancies: list[dict]) -> None:
        """
        Deletes vacancies from the file.

        Args:
        vacancies (list[dict]): A list of vacancies to delete.

        Returns:
        None

        Notes:
        The data is read from the file, vacancies are deleted from the list, and then the data is saved to the file.
        """
        data: list = FileHelper.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if vacancy in data:
                data.remove(vacancy)
        FileHelper.save_data(VACANCIES_DATA_PATH, data)
