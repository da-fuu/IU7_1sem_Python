# Жаринов Михаил ИУ7-12Б Лабораторная работа №13
# База данных

import os
import struct
from utils import get_size
import initialize
import output
import append_entry
import delete_entry
import find_one
import find_two


def check_filename(filename):
    existence = os.path.isfile(filename)
    try:
        file = open(filename, 'ab')
    except OSError:
        return False
    else:
        file.close()
        if not existence:
            os.remove(filename)
        return True


def check_initialization(filename, size_target):
    if not os.path.isfile(filename):
        return False
    size = get_size(filename)
    return size > 0 and size % size_target == 0


def print_menu():
    print('0. Завершить программу.')
    print('1. Выбрать файл для работы.')
    print('2. Инициализировать базу данных.')
    print('3. Вывести содержимое базы данных.')
    print('4. Добавить запись в базу данных.')
    print('5. Удалить запись из базы данных.')
    print('6. Поиск по одному полю.')
    print('7. Поиск по двум полям.')


def main():
    structure = '!30s22sB'
    size = struct.calcsize(structure)

    operations = [
        initialize.main,
        output.main,
        append_entry.main,
        delete_entry.main,
        find_one.main,
        find_two.main
    ]
    filename = ''
    initialized = False
    num_op = len(operations) + 1
    while True:
        print_menu()
        input_choose = input(f'Введите число от 0 до {num_op}: ').strip()
        if not (input_choose.isdigit() and 0 <= int(input_choose) <= num_op):
            print('Введите корректное число!')
            continue
        choose = int(input_choose)
        if choose == 0:
            return
        if choose > 1 and filename == '':
            print('Сначала введите имя файла!')
            continue
        if choose > 2 and not initialized:
            print('Сначала проинициализируйте БД!')
            continue
        if choose == 1:
            new_filename = input('Введите путь файла: ')
            while not check_filename(new_filename):
                new_filename = input('Введите корректный путь файла: ')
            if os.path.exists(new_filename):
                ans = input('Файл уже существует, вы уверены? y/n: ')
                if ans != 'y':
                    continue
            filename = new_filename
            initialized = check_initialization(filename, size)
        else:
            operations[choose-2](filename, structure)
            initialized = check_initialization(filename, size)


if __name__ == '__main__':
    main()
