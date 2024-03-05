import json


class FileHelper:
    """
    A class for working with JSON files.
    """

    @staticmethod
    def read_file(path: str) -> list:
        """
        Reads data from a JSON file and returns it as a list.

        Args:
        path (str): The path to the file.

        Returns:
        list: A list containing the data from the file.

        Notes:
        If the file is empty, the function returns an empty list.
        """
        data: list = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("File was empty")
        finally:
            return data

    @staticmethod
    def save_data(path: str, data: list) -> None:
        """
        Saves data to a file in JSON format.

        Args:
        path (str): The path to the file.
        data (list): A list containing the data to be saved.

        Returns:
        None

        Notes:
        The data is saved to the file with an indent of 4 spaces and without ASCII encoding.
        """
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
