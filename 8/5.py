# Жаринов Михаил ИУ7-12Б Лабораторная работа №8
# Найти максимальное значение в квадратной матрице над главной диагональю и минимальное под побочной диагональю

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
    # Если ввод успешен...
    # Поиск максимального значения над главной диагональю
    max_el = matrix[0][1]
    for i in range(length):
        for j in range(i + 1, length):
            max_el = max(max_el, matrix[i][j])
    # Поиск минимального значения под побочной диагональю
    min_el = matrix[1][-1]
    for i in range(length):
        for j in range(length - i, length):
            min_el = min(min_el, matrix[i][j])
    # Блок вывода
    print('Максимальное значение над главной диагональю:', max_el)
    print('Минимальное значение под побочной диагональю:', min_el)
