# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Работа с матрицами по алгоритму

# Блок ввода
len_y = int(input('Введите кол-во строк матриц: '))
matrix_z = []
for i in range(len_y):
    matrix_z.append([int(x) for x in input('Введите {}-ую строку матрицы Z через пробелы: '.format(i + 1)).split()])
    # noinspection PyUnboundLocalVariable
    if i == 0:
        len_x_z = len(matrix_z[0])
    # Проверка корректности ввода
    elif len(matrix_z[-1]) != len_x_z:
        print('Введено некорректное количество значений в строке!')
        break
else:
    # Если ввод успешен...
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
        # Заполнение списка G
        lst_g = []
        for i in range(len_y):
            cnt = len([x for x in matrix_d[i] if x > sum(matrix_z[i])])
            lst_g.append(cnt)
        # Расчет максимального элемента списка G
        maxcnt = max(lst_g)

        # Блок вывода
        print('Матрица Z:')
        for row in matrix_z:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()

        print('Матрица D до преобразования:')
        for row in matrix_d:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()

        # Умножение матрицы D
        for i in range(len_y):
            for j in range(len_x_d):
                matrix_d[i][j] *= maxcnt

        print('Матрица D после преобразования:')
        for row in matrix_d:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()
        print('Список G: ', *lst_g)
