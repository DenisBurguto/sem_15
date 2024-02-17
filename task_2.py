# Задание No2
# 📌 На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging


def my_dec_to_log(func):
    output_file = func.__name__ + ".log"
    log = logging.getLogger(func.__name__)
    logging.basicConfig(level=logging.NOTSET)
    file_handler = logging.FileHandler(output_file, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    def wrapper(*args, **kwargs):
        dic = {'args': args}
        for key, value in kwargs.items():
            dic[f'{key}'] = value
        result = func(*args, **kwargs)
        dic['result'] = result
        log.info(dic)
        return result
    return wrapper


@my_dec_to_log
def my_func(*args, **kwargs):
    return [i ** power for i in args for power in kwargs.values()]


@my_dec_to_log
def sum_elements(*args):
    return sum(args)


if __name__ == '__main__':
    my_func(9, 32, 23324242, power=2)
    my_func(5, power=4)
    my_func(88888, power=9)

    sum_elements(9, 333, 434)
    sum_elements(99, 33, 4)
