# Задание No1
# 📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(level=logging.NOTSET, filename='log.log', filemode='a', encoding='utf-8')
logger = logging.getLogger(__name__)


def division(a, b):
    if b == 0:
        logger.error("ZeroDivisionError")
    else:
        return a / b


if __name__ == '__main__':
    print(division(3, 2))
    print(division(3, 0))