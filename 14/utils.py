def get_size(filename):
    with open(filename, 'rb') as file:
        file.seek(0, 2)
        size = file.tell()
        return size


def ask_for_entry(ind):
    surname = input('Введите фамилию {:}-ого студента: '.format(ind)).strip()
    while not surname or len(surname) > 15:
        surname = input('Введите корректную фамилию {:}-ого студента: '.format(ind)).strip()
    group = input('Введите группу {:}-ого студента: '.format(ind)).strip()
    while not group or len(group) > 11:
        group = input('Введите корректную группу {:}-ого студента: '.format(ind)).strip()
    age = input('Введите возраст {:}-ого студента: '.format(ind)).strip()
    while not (age.isdigit() and 256 > int(age) > 0):
        age = input('Введите корректный возраст {:}-ого студента: '.format(ind)).strip()
    return surname.encode(), group.encode(), int(age)


def print_head():
    print('-' * 39)
    print('|{:^15}|{:^11}|{:^9}|'.format('Фамилия', 'Группа', 'Возраст'))
    print('-' * 39)


def print_entry(entry):
    print('|{:^15}|{:^11}| {:<8}|'.format(entry[0].decode().rstrip('\x00'), entry[1].decode().rstrip('\x00'),
                                          str(entry[2])))


def check_column_num(column: str):
    return column.isdigit() and 0 < int(column) <= 4


def check_target(target: str, column: int):
    if column == 0:
        return 0 < len(target) <= 15
    if column == 1:
        return 0 < len(target) <= 11
    if column == 2:
        return target.isdigit() and 256 > int(target) > 0


def check_field(field, target, column):
    if column == 2:
        return field == int(target)
    return field.decode().rstrip('\x00') == target
