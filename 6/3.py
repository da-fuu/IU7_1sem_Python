# Жаринов Михаил ИУ7-12Б Лабораторная работа №6
# Поиск к-го экстремума в списке

# Блок ввода
lst = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
k = int(input('Введите номер экстремума: '))

# Инициализация счетчика
curr_k = 0
for i in range(len(lst) - 2):
    # Если найден экстремум
    if lst[i] > lst[i + 1] < lst[i + 2] or lst[i] < lst[i + 1] > lst[i + 2]:
        # то прибавить 1 к счетчику
        curr_k += 1
    # если найден искомый экстремум
    if curr_k == k:
        # то вывести его
        print('К-тый экстремум:', lst[i + 1])
        break
else:
    # Если в списке меньше чем К экстремумов, то вывести соотв сообщение
    print('В списке меньше чем К экстремумов')
