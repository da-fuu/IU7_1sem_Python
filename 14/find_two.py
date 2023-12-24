def main(filename):
    first = 0
    column = input('Введите номера полей поиска через пробел: ').split()
    while not (len(column) == 2 and all([i.isdigit() and 0 < int(i) <= 4 for i in column])):
        column = input('Введите корректные два номера полей поиска через пробел: ').split()
    column = [int(i) - 1 for i in column]
    targets = []
    for i in column:
        target = input('Введите значение для поиска в {:}-ом столбце: '.format(i+1)).strip()
        while not (target and (target.isdigit() if i == 2 else True) and (check_float(target) if i == 3 else True)):
            target = input('Введите корректное значение для поиска в {:}-ом столбце: '.format(i+1)).strip()
        targets.append(target if i != 3 else str(round(float(target), 5)))
    with open(filename, 'r') as file:
        for entry in file:
            if entry.split(';')[column[0]] == targets[0] and entry.split(';')[column[1]] == targets[1]:
                if not first:
                    first = 1
                    print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format('Фамилия', 'Группа', 'Возраст', 'Коофициент'))
                print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format(*entry.split(';')))
    if not first:
        print('Ничего не найдено')
