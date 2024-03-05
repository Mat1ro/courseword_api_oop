from file_editor.json_editor import JsonHelper
from vacancies.vacancies_API.headhunter import HeadhunterAPI
from vacancies.vacancies_API.superjob import SuperJobAPI

headHunter = HeadhunterAPI()
superJob = SuperJobAPI()


def output_vacancy(vacancy):
    print(f'Должность - {vacancy["position"]}\n'
          f'Ссылка - {vacancy["url"]}\n'
          f'Зарплата {vacancy["salary_from"]} - {vacancy["salary_to"]}\n'
          f'Описание - {vacancy["description"]}\n'
          f'Требования - {vacancy["must_know"]}\n')


def find_by_query(search_engine, query: str):
    return search_engine.get_vacancies(query)


def user_interaction():
    search_engine = int(input("Где хочешь посмотреть вакансию, введи 1 или 2:\n"
                              "1 - Headhunter\n"
                              "2 - SuperJob\n"))
    query = input("На какую профессию ищешь вакансии?\n")
    if search_engine == 1:
        result = find_by_query(headHunter, query)
    else:
        result = find_by_query(superJob, query)
    for vacancy in result:
        output_vacancy(vacancy)

    JsonHelper.add_vacancy(result)
    salary_from, salary_to = map(int, input("Введи в каком диапазоне хочешь видеть вакансии:\n"
                                            "В формате '1000-2000'\n").split('-'))
    for vacancy in JsonHelper.get_vacancies_by_salary(salary_from, salary_to):
        output_vacancy(vacancy)
    JsonHelper.delete_vacancy(result)

    # Получение top N вакансий
    n = int(input())
    query = input()
    headHunter.get_top_n_vacancies(n, query)
    superJob.get_top_n_vacancies(n, query)


if __name__ == "__main__":
    user_interaction()
