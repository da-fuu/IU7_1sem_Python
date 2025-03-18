def main(filename):
    print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format('Фамилия', 'Группа', 'Возраст', 'Коофициент'))
    with open(filename, 'r') as file:
        for entry in file:
            print('|{:^15}|{:^11}|{:^9}|{:^10}|'.format(*entry.split(';')))
