def main(filename):
    first = 0
    column = input('Введите номер поля поиска: ').strip()
    while not (column.isdigit() and 0 < int(column) <= 4):
        column = input('Введите корректный номер поля поиска: ').strip()
    target = input('Введите значение для поиска: ').strip()
    if column == '4':
        while not check_float(target):
            target = input('Введите корректное значение для поиска: ').strip()
        target = str(round(float(target), 5))
    elif column == '3':
        while not target.isdigit():
            target = input('Введите корректное значение для поиска: ').strip()
    column = int(column) - 1

    with open(filename, 'r') as file:
        for entry in file:
            if entry.split(';')[column] == target:
                if not first:
                    first = 1
                    print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format('Фамилия', 'Группа', 'Возраст', 'Коофициент'))
                print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format(*entry.split(';')))
    if not first:
        print('Ничего не найдено')
