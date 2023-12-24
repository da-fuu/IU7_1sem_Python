# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Вычисление максимального элемента данных строк матрицы и вычисление среднего арифметического этих элементов

# Блок ввода
len_y = int(input('Введите количество строк матрицы: ').strip())
matrix_d = []
for i in range(len_y):
    matrix_d.append([int(x) for x in input('Введите {}-ую строку матрицы D через пробелы: '.format(i + 1)).split()])
    # noinspection PyUnboundLocalVariable
    if i == 0:
        len_x_d = len(matrix_d[0])
    # Проверка корректности ввода
    elif len(matrix_d[-1]) != len_x_d:
        print('Введено некорректное количество значений в строке!')
        break
else:
    # Если ввод успешен…
    # Ввод списка I
    lst_i = list(map(int, input('Введите элементы списка I через пробел: ').split()))
    # Обработка некорректного ввода
    if len(lst_i) > len(set(lst_i)) or len(lst_i) > len_y or max(lst_i) > len_y - 1 or min(lst_i) < 0:
        print('Введены некорректные индексы строк массива!')
    else:
        # Заполение списка R
        r = []
        for ind in lst_i:
            r.append(max(matrix_d[ind]))
        # Расчет среднего арифметического
        avg = sum(r) / len(r)

        # Блок вывода
        print('Матрица D:')
        for row in matrix_d:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()
        print('Список I:\n', *lst_i)
        print('Список R:\n', *r)
        print('Среднее арифметическое элементов списка R: {:.6g}'.format(avg))
