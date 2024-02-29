# # Creating a class instance to work with the APIs of job search sites
# hh_api = HeadHunterAPI()
# superjob_api = SuperJobAPI()
#
# # Getting job vacancies from different platforms
# hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")
#
# # Creating a class instance to work with vacancies
# vacancies = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Saving information about vacancies to a file
# json_helper = JSONHelper()
# json_helper.add_vacancy(vacancies)
# json_helper.get_vacancies_by_salary("100 000-150 000 руб.")
# json_helper.delete_vacancy(vacancies)
#
# # Function to interact with the user
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Enter a search query: ")
#     top_n = int(input("Enter the number of vacancies to display in top N: "))
#     filter_words = input("Enter keywords to filter vacancies: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Vacancies matching the selected criteria are not found.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()