# Жаринов Михаил ИУ7-12Б Лабораторная работа №13
# База данных

import os
import initialize
import output
import append_entry
import find_one
import find_two
from check_float import main as check_float

def check_filename(filename):
    existance = os.path.isfile(filename)
    try:
        file = open(filename, 'a')
    except OSError:
        return False
    else:
        file.close()
        if not existance:
            os.remove(filename)
        return True


def check_initialization(filename):
    if not os.path.isfile(filename):
        return False
    with open(filename, 'r') as file:
        for entry in file:
            fields = entry.split(';')
            if not (len(fields) == 5 and fields[2].isdigit() and check_float(fields[3])):
                return False
    return True


def print_menu():
    print('0. Завершить программу.')
    print('1. Выбрать файл для работы.')
    print('2. Инициализировать базу данных.')
    print('3. Вывести содержимое базы данных.')
    print('4. Добавить запись в конец базы данных.')
    print('5. Поиск по одному полю.')
    print('6. Поиск по двум полям.')


def main():
    operations = [
        initialize.main,
        output.main,
        append_entry.main,
        find_one.main,
        find_two.main
    ]
    filename = ''
    initialized = False
    while True:
        print_menu()
        input_choose = input('Введите число от 0 до 6: ').strip()
        if not (input_choose.isdigit() and 0 <= int(input_choose) <= 6):
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
            initialized = check_initialization(filename)
        else:
            operations[choose-2](filename)
            if choose == 2:
                initialized = True


if __name__ == '__main__':
    main()
