# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Замена всех англ. гласных на точки в матрице символов

# Блок ввода
len_y = int(input('Введите кол-во строк матрицы: '))
matrix = []
for i in range(len_y):
    matrix.append(input('Введите {}-ую строку матрицы через пробелы: '.format(i + 1)).split())
    # noinspection PyUnboundLocalVariable
    if i == 0:
        len_x = len(matrix[0])
    # Проверка корректности ввода
    elif len(matrix[-1]) != len_x:
        print('Введено некорректное количество значений в строке!')
        break
    for c in matrix[i]:
        if len(c) != 1:
            print('Введен некорректный элемент!')
            break
else:
    # Если ввод успешен...
    # Промежуточный вывод
    print('Исходная матрица: ')
    for row in matrix:
        for el in row:
            print('{:^3}'.format(el), end='')
        print()
    # Замена англ. гласных на точки
    for i in range(len_y):
        for j in range(len_x):
            if matrix[i][j].lower() in 'eyuioa':
                matrix[i][j] = '.'
    # Блок вывода
    print('Итоговая матрица: ')
    for row in matrix:
        for el in row:
            print('{:^5}'.format(el), end='')
        print()
