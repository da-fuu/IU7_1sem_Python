# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Вывод i-того среза по второму индексу(Y)

# Блок ввода
len_x = int(input('Введите кол-во матриц: '))
len_y = int(input('Введите кол-во строк матриц: '))
len_z = int(input('Введите кол-во столбцов матриц: '))
space = []
for j in range(len_x):
    matrix = []
    for i in range(len_y):
        matrix.append(
            [int(x) for x in input('Введите {} строку {} матрицы через пробелы: '.format(i + 1, j + 1)).split()])
        # Обработка некорректного ввода
        if len(matrix[i]) != len_z:
            print('Введено некорректное количество значений в строке!')
            break
    else:
        # Добавление матрицы в список матриц
        space.append(matrix)
        continue
    # Обработка некорректного ввода
    break

else:
    ind = int(input('Введите номер среза: '))

    # Вывод нужного среза
    print('{}-ый срез: '.format(ind))
    for matrix in space:
        for el in matrix[ind]:
            print('{:^5g}'.format(el), end='')
        print()
