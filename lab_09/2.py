# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Программа для поворота квадратной матрицы на 90 градусов
# по часовой стрелке и против часовой стрелки

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
    # Поворот по часовой стрелке
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i] = \
                matrix[length - j - 1][i], matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][
                    length - j - 1]

    # Вывод промежуточной матрицы
    print('Повернутая матрица:')
    for row in matrix:
        for el in row:
            print('{:^5g}'.format(el), end='')
        print()

    # Поворот обратно
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            matrix[i][j], matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i] = \
                matrix[j][length - i - 1], matrix[length - i - 1][length - j - 1], matrix[length - j - 1][i], matrix[i][
                    j]

    # Блок вывода
    print('Итоговая матрица:')
    for row in matrix:
        for el in row:
            print('{:^5g}'.format(el), end='')
        print()
