# Жаринов Михаил ИУ7-12Б Лабораторная работа №8
# Выполнить транспонирование квадратной матрицы

# Блок ввода
length = int(input('Введите кол-во строк (столбцов): '))
matrix = []
for i in range(length):
    matrix.append([int(x) for x in input('Введите {}-ую строку через пробелы: '.format(i + 1)).split()])
    # Проверка корректности ввода
    if len(matrix[-1]) != length:
        print('Введено некорректное количество значений в строке!')
        break
else:
    # Если ввод успешен…
    # То транспонируем матрицу
    for i in range(length):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Блок вывода
    print('Получившаяся матрица:')
    for line in matrix:
        for elem in line:
            print('{:<5g}'.format(elem), end='')
        print()
