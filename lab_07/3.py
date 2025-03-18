# Жаринов Михаил ИУ7-12Б Лабораторная работа №7
# Удаление элемента из списка

length = int(input('Введите длину списка: '))
lst = []
for i in range(length):
    lst.append(input('Введите {}-ый элемент: '.format(i + 1)))

max_space = 0
ind = -1
for i in range(length):
    curr_max = 0
    for j in range(len(lst[i])):
        if lst[i][j] == ' ':
            curr_max += 1
        else:
            if curr_max > max_space:
                max_space = curr_max
                ind = i
            curr_max = 0
    if curr_max > max_space:
        max_space = curr_max
        ind = i
if ind > -1:
    print('Элемент с максимальным кол-вом подряд идущих пробелов:\n"', lst[ind], '"', sep='')
else:
    print('Ни в одном элементе нет пробелов')
