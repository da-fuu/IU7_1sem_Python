from check_float import main as check_float


def main(filename):
    with open(filename, 'a') as file:
        surname = input('Введите фамилию студента: ').strip()
        while not surname or len(surname) > 15:
            surname = input('Введите корректную фамилию студента: ').strip()
        group = input('Введите группу студента: ').strip()
        while not group or len(group) > 11:
            group = input('Введите корректную группу студента: ').strip()
        age = input('Введите возраст студента: ').strip()
        while not (age.isdigit() and 1000 > int(age) > 0):
            age = input('Введите корректный возраст студента: ').strip()
        koef = input('Введите коофициент студента: ').strip()
        while not (koef.isdigit() and check_float(koef)):
            koef = input('Введите корректный коофициент студента: ').strip()
        file.write(';'.join([surname, group, age, str(round(float(koef), 5)), '\n']))
