# Задание No4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime, date

START = 1
WEEK = 7
FORMAT ='{funcName} -{asctime} -{msg}'

logging.basicConfig(level=logging.ERROR, filename='errors.log', filemode='a', encoding='utf-8', format=FORMAT, style='{')
log = logging.getLogger(__name__)


def get_date_from_text(text: str):
    year = datetime.now().year
    ru_days = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'cуббота': 5, 'воскресенье': 6}
    ru_months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    try:
        day_count, *_, day_ru, mounth_ru = text.split(' ')
    except ValueError:
        log.error(f"Invalid input {text}")
        exit(1)
    try:
        day_int = ru_days[day_ru]
    except KeyError:
        log.error(f"Invalid input {text}: name of the day")
        exit(1)
    try:
        month_int = ru_months[mounth_ru]
    except KeyError:
        log.error(f"Invalid input {text}: name of the month")
        exit(1)
    try:
        day_count_int = int(day_count[0])
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
    print(get_date_from_text("1 - й четверг ноября"))
    print(get_date_from_text("9- я cуббота мая"))
