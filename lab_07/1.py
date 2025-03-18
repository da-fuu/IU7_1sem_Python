# Жаринов Михаил ИУ7-12Б Лабораторная работа №7
# Удаление элемента из списка

# Блок ввода
lst = [int(i) for i in input('Введите элементы списка через пробел: ').split()]

curr_elem = 0
num_del = 0
for j in range(len(lst)):
    if lst[curr_elem] % 2 == 0:
        for i in range(curr_elem, len(lst) - 1):
            lst[i] = lst[i + 1]
        num_del += 1
    else:
        curr_elem += 1

# Блок вывода
print('Полученный список:', end=' ')
for i in range(len(lst) - num_del):
    print(lst[i], end=' ')
