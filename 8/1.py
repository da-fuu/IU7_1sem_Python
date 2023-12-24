# Жаринов Михаил ИУ7-12Б Лабораторная работа №8
# Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов

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
    max_same = 0
    ind = 0
    for i in range(len_y):
        # Обнуление текущего максимума
        curr_max = 0
        for j in range(1, len_x):

            if matrix[i][j] == matrix[i][j - 1]:
                # Если элемент равен предыдущему то прибавить 1 к счетчику
                curr_max += 1
            else:
                # Если текущая длина больше макимальной
                if curr_max > max_same:
                    # То обновить счетчик
                    max_same = curr_max
                    # Сохранить индекс элемента
                    ind = i
                # Обнуление текущего максимума
                curr_max = 0
                # Проверка последней последовательности
        if curr_max > max_same:
            max_same = curr_max
            ind = i
    # Блок вывода
    print('Строка, имеющая наибольшее количество подряд идущих одинаковых элементов:')
    for elem in matrix[ind]:
        print('{:<5g}'.format(elem), end='')
