# Поиск по одному полю

from utils import check_column_num, check_target, get_size, print_head, print_entry, check_field
from struct import unpack, calcsize


def main(filename, structure):
    # Ввод искомых значений
    column = input('Введите номер поля поиска: ').strip()
    while not check_column_num(column):
        column = input('Введите корректный номер поля поиска: ').strip()
    column = int(column) - 1
    target = input('Введите значение для поиска: ').strip()
    while not check_target(target, column):
        target = input('Введите корректное значение для поиска: ').strip()

    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    first = False

    # Поиск и вывод
    with open(filename, 'rb') as file:
        for i in range(lines):
            entry = file.read(entry_size)
            entry = unpack(structure, entry)
            if check_field(entry[column], target, column):
                if not first:
                    first = True
                    print_head()
                print_entry(entry)
    if not first:
        print('Ничего не найдено')
