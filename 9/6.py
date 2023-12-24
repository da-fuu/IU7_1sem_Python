# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Выполнение построчного перемножения матриц и расчет суммы элементов столбцов

# Блок ввода
len_y = int(input('Введите количество строк матриц: ').strip())
len_x = int(input('Введите количество столбцов матриц: ').strip())
# Ввод матрицы А
matrix_a = []
for i in range(len_y):
    matrix_a.append([int(x) for x in input('Введите {}-ую строку матрицы А через пробелы: '.format(i + 1)).split()])
    # Проверка корректности ввода
    if len(matrix_a[-1]) != len_x:
        print('Введено некорректное количество значений в строке!')
        break
else:
    # Ввод матрицы В
    matrix_b = []
    for i in range(len_y):
        matrix_b.append([int(x) for x in input('Введите {}-ую строку матрицы В через пробелы: '.format(i + 1)).split()])
        # Проверка корректности ввода
        if len(matrix_b[-1]) != len_x:
            print('Введено некорректное количество значений в строке!')
            break
    else:
        # Заполнение матрицы С
        matrix_c = []
        for i in range(len_y):
            matrix_c.append([])
            for j in range(len_x):
                matrix_c[i].append(matrix_a[i][j] * matrix_b[i][j])
        # Заполнение списка V
        lst_v = []
        for j in range(len_x):
            curr = 0
            for i in range(len_y):
                curr += matrix_c[i][j]
            lst_v.append(curr)

        # Блок вывода
        print('Матрица A:')
        for row in matrix_a:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()

        print('Матрица B:')
        for row in matrix_b:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()

        print('Матрица C:')
        for row in matrix_c:
            for el in row:
                print('{:^5g}'.format(el), end='')
            print()

        print('Список V: ', *lst_v)
