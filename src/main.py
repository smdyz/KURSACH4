from src.classes import GetVacancy
from src.classes import CertainVacancy
from src.classes import SalaryVacancy

import json


def for_usr(q) -> None:
    if q.isalpha() or 3 < int(q) < 1:
        print("Указан некорректный номер запроса")
    else:
        q = int(q)
        search = input("Введите поисковый запрос: ")
        if q == 1 or q == 3:
            """вызывает класс в который передается поисковый запрос"""
            get = GetVacancy(search)
            for i in get.get_vacancies:
                print(f"id - {i['id']}\n"
                      f"Название вакансии - {i['name']}\n"
                      f"Зарплата - {i['salary']}\n"
                      f"Город - {i['city']}\n"
                      f"Описание - {i['description']}"
                      f"Ссылка - {i['url']}\n")

        if q == 2:
            top = input("Сколько вакансий вы хотите получить - ")
            """вызывает класс в который передается, какой топ вывести"""
            top_salary = SalaryVacancy(search)
            top_salary = top_salary.sorted_salary(10)
            s = 1
            for i in top_salary:
                print(f"{s} место\n"
                      f"Зарплата - {i['salary']}\n"
                      f"Название вакансии - {i['name']}\n"
                      f"Город - {i['city']}\n"
                      f"Ссылка - {i['url']}\n")
                s += 1

        if q == 3:
            """вызывает класс в который передается id искомой вакансии"""
            search_id = int(input("введите id понравившейся вакансии, чтобы узнать больше информации: "))
            id_vac = CertainVacancy(search, search_id)
            id_vac.full_info()


question = input("Это небольшая программа для поиска вакансий на HH.ru.\n"
                 "Введите номер интересующего вас вопроса, чтобы продолжить:\n"
                 "1 Ввести поисковый запрос для запроса вакансий из hh.ru\n"
                 "2 Получить топ N вакансий по зарплате\n"
                 "3 Полная информация о вакансии\n")

for_usr(question)
