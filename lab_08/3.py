# Жаринов Михаил ИУ7-12Б Лабораторная работа №8
# Найти столбец, имеющий наибольшее количество простых чисел

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
    #
    max_column = 0
    ind = -1
    #
    for j in range(len_x):
        curr = 0
        #
        for i in range(len_y):
            is_prime = True
            el = matrix[i][j]
            #
            if el < 2:
                is_prime = False
            for k in range(2, int(el ** 0.5) + 1):
                if el % k == 0:
                    is_prime = False
                    break
            if is_prime:
                #
                curr += 1
        #
        if curr > max_column:
            max_column = curr
            ind = j

    # Блок вывода
    if ind > -1:
        print('Столбец, имеющий наибольшее количество простых чисел:')
        for line in matrix:
            print(line[ind])
    else:
        print('Простых чисел нет')
