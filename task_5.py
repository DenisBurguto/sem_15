# Задание No5
# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в
# месяце день недели, текущий день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import argparse
import logging
from datetime import datetime, date

START = 1
WEEK = 7
FORMAT = '{funcName} -{asctime} -{msg}'

logging.basicConfig(level=logging.ERROR, filename='errors.log', filemode='a', encoding='utf-8', format=FORMAT,
                    style='{')
log = logging.getLogger(__name__)


def get_date_from_text(*args):
    text = args
    year = datetime.now().year
    ru_days = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'cуббота': 5, 'воскресенье': 6}
    ru_months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    try:
        day_count, *_, day_ru, mounth_ru = args
    except ValueError:
        try:
            day_count, *_, day_ru, mounth_ru = args[0].split()
        except ValueError:
            log.error(f"Invalid input {text}")
            exit(1)

    try:
        day_int = ru_days[day_ru]
    except KeyError:
        try:
            day_int = int(day_ru)
        except ValueError:
            log.error(f"Invalid input {text}: name of the day")
            exit(1)
    try:
        month_int = ru_months[mounth_ru]
    except KeyError:
        try:
            month_int = int(mounth_ru)
        except ValueError:
            log.error(f"Invalid input {text}: name of the month")
            exit(1)
    try:
        day_count_int = int(day_count[0])
    except TypeError:
        try:
            day_count_int = int(day_count)
        except ValueError:
            log.error(f"Invalid input {text}: count of the day")
            exit(1)

    start = date(year, month_int, START)
    if start.weekday() == day_int:
        try:
            return date(year, month_int, (START + WEEK * day_count_int - WEEK))
        except ValueError:
            log.error(f"Invalid input {text}: count of the day")
            exit(1)
    elif start.weekday() < day_int:
        try:
            return date(year, month_int, (day_int - start.weekday() + WEEK * day_count_int - WEEK + 1))
        except ValueError:
            log.error(f"Invalid input {text}: count of the day")
            exit(1)
    elif start.weekday() > day_int:
        try:
            return date(year, month_int, (start.weekday() - day_int + WEEK * day_count_int - 1))
        except ValueError:
            log.error(f"Invalid input {text}: count of the day")
            exit(1)


if __name__ == '__main__':
    # print(get_date_from_text("1-й четверг ноября"))
    parser = argparse.ArgumentParser(description='getting date from text')
    parser.add_argument('param', metavar='text',
                        nargs='*', default=(1, datetime.now().weekday(), datetime.now().month),
                        help='text like "1-й четверг ноября" or use digits instead ')
    args_in = parser.parse_args()
    print(get_date_from_text(*args_in.param))
