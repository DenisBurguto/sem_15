# Задание No6
# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
import os.path
from collections import namedtuple

FORMAT = '{funcName} -{asctime} -{msg}'

logging.basicConfig(level=logging.NOTSET, filename='path.log', filemode='a', encoding='utf-8', format=FORMAT,
                    style='{')
log = logging.getLogger(__name__)
File = namedtuple('File', ['extension', 'file_name', 'parent_dir'])
Folder = namedtuple('Folder', ['dir_name', 'dir_access', 'parent_dir'])


def parse_path():
    results = []
    parser = argparse.ArgumentParser(description='getting path  from console')
    parser.add_argument('file_path', type=str,
                        help='enter path to file or directory ')
    args_in = parser.parse_args()
    for root, dirs, files in os.walk(args_in.file_path):
        for file in files:
            file_name, extension = os.path.splitext(file)
            parent_dir = root.split('/')[-1]
            file = File(extension, file_name, parent_dir)
            results.append(file)
            log.info(file)
        for dir_ in dirs:
            path = os.path.join(root, dir_)
            dir_name = dir_
            if os.access(path, os.X_OK):
                dir_access = 'X'
            elif os.access(path, os.W_OK):
                dir_access = 'W'
            else:
                dir_access = 'R'
            parent_dir = root.split('/')[-1]
            folder = Folder(dir_name, dir_access, parent_dir)
            results.append(folder)
            log.info(folder)
        return results


if __name__ == '__main__':
    print(parse_path())
