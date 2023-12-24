from utils import check_column_num, check_target, get_size, print_head, print_entry, check_field
from struct import unpack, calcsize


def main(filename, structure):
    columns = input('Введите номера полей поиска через пробел: ').split()
    while not (len(columns) == 2 and all([check_column_num(i) for i in columns])):
        columns = input('Введите корректные два номера полей поиска через пробел: ').split()
    columns = [int(i) - 1 for i in columns]
    targets = []
    for i in columns:
        target = input('Введите значение для поиска в {:}-ом столбце: '.format(i + 1)).strip()
        while not check_target(target, i):
            target = input('Введите корректное значение для поиска в {:}-ом столбце: '.format(i + 1)).strip()
        targets.append(target)

    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    first = False

    with open(filename, 'rb') as file:
        for i in range(lines):
            entry = file.read(entry_size)
            entry = unpack(structure, entry)
            if all(check_field(entry[columns[j]], targets[j], columns[j]) for j in range(2)):
                if not first:
                    first = True
                    print_head()
                print_entry(entry)
    if not first:
        print('Ничего не найдено')
