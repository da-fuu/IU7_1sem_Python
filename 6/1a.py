# Жаринов Михаил ИУ7-12Б Лабораторная работа №6
# Добавление элемента в список

# Блок ввода
lst = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
el = int(input('Введите дополнительный элемент: '))
ind = int(input('Введите индекс дополнительного элемента: '))

# Добавление элемента в список
lst.insert(ind, el)

# Блок вывода
print('Полученный список:', *lst)
