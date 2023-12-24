# Жаринов Михаил ИУ7-12Б Лабораторная работа №10
# Демонстрация работы метода шейкер-сортировки

# Подключение модулей
import time
import random


# Шейкер-сортировка массива с подсчетом времени и количества перестановок
def shaker_sort(lst):
    temp = lst.copy()
    replaces = 0
    start = time.perf_counter_ns()
    for i in range(len(temp) - 1, 0, -1):
        for j in range(i, 0, -1):
            if temp[j] < temp[j - 1]:
                temp[j], temp[j - 1] = temp[j - 1], temp[j]
                replaces += 1

        for j in range(i):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                replaces += 1
    stop = time.perf_counter_ns()

    dur = (stop - start) / 10 ** 6
    return temp, dur, replaces


# Создание словаря необходимой информации о сортировке 3 списков заданной длины
def get_metrics(lens):
    metrics = {'sorted': [], 'random': [], 'reversed': []}
    for n in lens:
        # Случайный список
        lst = []
        for i in range(n):
            lst.append(random.randint(-n, n))
        rand_result = shaker_sort(lst)
        # Упорядоченный список
        lst = rand_result[0]
        sort_result = shaker_sort(lst)
        # Обратно упорядоченный список
        lst = lst[::-1]
        revers_result = shaker_sort(lst)
        # Сохранение необходимых данных
        metrics['sorted'].append({'time': sort_result[1], 'replaces': sort_result[2], 'name': 'Упорядоченный список'})
        metrics['random'].append({'time': rand_result[1], 'replaces': rand_result[2], 'name': 'Случайный список'})
        metrics['reversed'].append(
            {'time': revers_result[1], 'replaces': revers_result[2], 'name': 'Обратно упор. список'})
    return metrics


# Печать таблицы
def print_table(metrics):
    # Печать шапки
    print('|{:}|{:^25}|{:^25}|{:^25}|'.format(' ' * 20, 'N1', 'N2', 'N3'))
    print('|' + '-' * 20 + '|' + ('-' * 12 + '|') * 6)
    print('|' + ' ' * 20 + '|' + ' время, мс  |перестановки|' * 3)
    print('|' + '-' * 20 + '|' + ('-' * 12 + '|') * 6)
    # Печать информации о трех списках разного вида
    for order in ['sorted', 'random', 'reversed']:
        print('|{:<20}|'.format(metrics[order][0]['name']), end='')
        # Печать информации о списках одного вида разной длины
        for n in range(3):
            print(' {:<11.5g}| {:<11.5g}|'.format(metrics[order][n]['time'], metrics[order][n]['replaces']), end='')
        print('\n|' + '-' * 20 + '|' + ('-' * 12 + '|') * 6)


# Ввод длин списков
def get_lengths():
    input_lens = input('Введите три длины списков через пробел: ')
    lens = []
    for s in input_lens.split():
        if not s.isdigit() or int(s) < 1:
            print('Введено некорректное число!')
            return
        lens.append(int(s))
    if len(lens) != 3:
        print('Введено некорректное число элементов!')
        return
    return tuple(lens)


# Ввод тестового списка
def get_list():
    lst = []
    input_list = input('Введите тестовый список через пробел: ')
    for s in input_list.split():
        if not s.removeprefix('-').isdigit():
            print('Введен некореектный элемент')
            return
        lst.append(int(s))
    if len(lst) == 0:
        print('Введите хотя бы один элемент')
        return
    return lst


# Основная функция
def main():
    user_list = get_list()
    if user_list is None:
        return

    # Вывод тестового списка
    print('Отсортированный список:')
    print(*(shaker_sort(user_list)[0]))

    lengths = get_lengths()
    if lengths is None:
        return

    metrics = get_metrics(lengths)

    print_table(metrics)


if __name__ == '__main__':
    main()
