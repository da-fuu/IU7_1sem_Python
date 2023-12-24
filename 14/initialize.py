from struct import pack


def main(filename, structure):
    entry = input('Введите количество строк: ').strip()
    while not (entry.isdigit() and int(entry) > 0):
        entry = input('Введите корректное количество строк: ').strip()
    entry = int(entry)
    with open(filename, 'wb') as file:
        for i in range(1, entry + 1):
            surname = input('Введите фамилию {:}-ого студента: '.format(i)).strip()
            while not surname or len(surname) > 15:
                surname = input('Введите корректную фамилию {:}-ого студента: '.format(i)).strip()
            group = input('Введите группу {:}-ого студента: '.format(i)).strip()
            while not group or len(group) > 11:
                group = input('Введите корректную группу {:}-ого студента: '.format(i)).strip()
            age = input('Введите возраст {:}-ого студента: '.format(i)).strip()
            while not (age.isdigit() and 256 > int(age) > 0):
                age = input('Введите корректный возраст {:}-ого студента: '.format(i)).strip()
            file.write(pack(structure, surname.encode(), group.encode(), int(age)))
