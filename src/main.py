from src.classes import GetVacancy
# from src.classes import KeyVacancy
from src.classes import SalaryVacancy


def for_usr(q: int) -> None:
    if q == 1:
        search = input("Введите поисковый запрос")
        """вызываем класс в который передам поисковый запрос"""
        get = GetVacancy(search)
    if q == 2:
        search = input("Введите поисковый запрос")
        top = input("Сколько вакансий вы хотите получить")
        """вызываем класс в который передам какой топ вывести"""
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
        word_in_desc = input("Введите ключевое слово")
        """вызываем класс в который передам ключевое слово из описания"""
    if 3 < q < 1:
        print("Указан некорректный номер запроса")


question = input("Это небольшая программа для поиска вакансий на HH.ru.\n"
                 "Введите номер интересующего вас вопроса, чтобы продолжить:\n"
                 "1 Ввести поисковый запрос для запроса вакансий из hh.ru\n"
                 "2 Получить топ N вакансий по зарплате (N запрашивать у пользователя)\n"
                 "3 Получить вакансии с ключевым словом в описании\n")

for_usr(int(question))

# a = {"a": 1, "b": 2}
#
# if "c" in a:
#     print("da")
# else:
#     print("net")
