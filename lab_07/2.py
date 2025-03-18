# Жаринов Михаил ИУ7-12Б Лабораторная работа №7
# Удаление элемента из списка

# Блок ввода
lst = [int(i) for i in input('Введите элементы списка через пробел: ').split()]

curr_elem = 0
for j in range(len(lst)):
    if lst[curr_elem] % 3 == 0:
        lst += [None]
        # Сдвиг элементов после искомого вправо
        for i in range(len(lst) - 1, curr_elem + 1, -1):
            lst[i] = lst[i - 1]
        # Запись искомого элемента
        lst[curr_elem + 1] = lst[curr_elem] * 2
        curr_elem += 1
    curr_elem += 1

# Блок вывода
print('Полученный список:', *lst)
