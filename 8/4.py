# Жаринов Михаил ИУ7-12Б Лабораторная работа №8
# Переставить местами столбцы с максимальной и минимальной суммой элементов


# Блок ввода
len_y = int(input('Введите кол-во строк: '))
matrix = []
for i in range(len_y):
    matrix.append([int(x) for x in input('Введите {}-ую строку через пробелы: '.format(i + 1)).split()])
    # noinspection PyUnboundLocalVariable
    if i == 0:
        len_x = len(matrix[0])
    # Проверка корректности ввода
    elif len(matrix[-1]) != len_x:
        print('Введено некорректное количество значений в строке!')
        break
else:
    # Если ввод успешен...
    # Блок вывода
    print('Получившаяся матрица:')
    for line in matrix:
        for elem in line:
            print('{:<5g}'.format(elem), end='')
        print()
