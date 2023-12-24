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
    print('|{:^15}|{:^11}|{:^9}'.format('Фамилия', 'Группа', 'Возраст'))
