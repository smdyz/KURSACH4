from src.classes import GetVacancy
from src.classes import SalaryVacancy
from src.classes import CertainVacancy
from src.main import for_usr

import json


def test_get_vacancies():
    g = GetVacancy("Сантехник")
    assert g.get_vacancies[:2] == [{'city': 'Санкт-Петербург',
                                    'description': 'Опыт работы от 3-х лет. Контроль показаний счетчиков. Знание '
                                                   'обслуживания тепловых узлов. Ответственность, '
                                                   'исполнительность.',
                                    'id': '93157544',
                                    'name': 'Дежурный слесарь-сантехник',
                                    'salary': {'currency': 'RUR', 'from': 60000, 'gross': False, 'to': 60000},
                                    'url': 'https://hh.ru/vacancy/93157544'},
                                   {'city': 'Санкт-Петербург',
                                    'description': 'Опыт работы монтажником СТС или слесарем-сантехником от 1 '
                                                   'года. Ответственность, исполнительность. Наличие образования '
                                                   'и подтверждающих документов для выполнения работ. ',
                                    'id': '93190900',
                                    'name': 'Сантехник-монтажник',
                                    'salary': {'currency': 'RUR', 'from': 300000, 'gross': True, 'to': 350000},
                                    'url': 'https://hh.ru/vacancy/93190900'}]


def test_sorted_vacancies():
    s = SalaryVacancy("Налоговый инспектор")
    assert s.sorted_salary(2) == [{'id': '93226541',
                                   'name': 'Главный государственный налоговый инспектор отдела выездных проверок, предпроверочного анализа',
                                   'salary': {'from': 80000, 'to': None, 'currency': 'RUR', 'gross': True},
                                   'url': 'https://hh.ru/vacancy/93226541',
                                   'description': 'Высшее образование по направлениям подготовки: экономика, бухгалтерский учет, юриспруденция, государственное и муниципальное управление, экономическая безопасность. Опыт работы в ИФНС.',
                                   'city': 'Санкт-Петербург'},
                                  {'id': '92182049',
                                   'name': 'Старший государственный налоговый инспектор контрольно-аналитического отдела',
                                   'salary': {'from': 80000, 'to': 100000, 'currency': 'RUR', 'gross': True},
                                   'url': 'https://hh.ru/vacancy/92182049',
                                   'description': 'опыт работы в контрольном блоке (КАО, ППА, ВНП, ОКП при проведении проверок НДС в части ст. 54.1) не менее...',
                                   'city': 'Москва'}]


def test_certain_vacancy():
    c = CertainVacancy("Бухгалтер", 7777)
    v = json.loads(c.full_info())
    assert v["name"] == "Бухгалтер"
    assert v["id"] == '7777'


# import sys
# from io import StringIO
#
#
# def test_main_func(capsys):
#     captured_output = StringIO()
#     sys.stdout = captured_output
#
#     for_usr(4)
#
#     sys.stdout = sys.__stdout__
#
#     captured = captured_output.getvalue().strip()
#     assert captured == "Указан некорректный номер запроса"
