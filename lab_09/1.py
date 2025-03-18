# Жаринов Михаил ИУ7-12Б Лабораторная работа №9
# Программа для заполнения матрицы по заданной формуле и определения среднего арифметического положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического

from math import sin

# Блок ввода
d = list(map(int, input('Введите элементы первого списка через пробел: ').split()))
f = list(map(int, input('Введите элементы второго списка через пробел: ').split()))

# Сохранение длины
len_d = len(d)
len_f = len(f)
# Создание пустой матрицы и списков
matrix = [[0] * len_f for i in range(len_d)]
av = []
l = []

for j in range(len_d):
	pos_cnt = 0
	pos_sum = 0

	for k in range(len_f):
		# Заполнение матрицы
		matrix[j][k] = sin(d[j] + f[k])
		# Расчет среднего арифметического положительных элементов
		if matrix[j][k] > 0:
			pos_cnt += 1
			pos_sum += matrix[j][k]

	# Инициализация переменных
	avg = -1
	l_cnt = len(matrix[j])
	# Обновление переменных
	if pos_cnt != 0:
		avg = pos_sum / pos_cnt
		l_cnt = 0
		for x in matrix[j]:
			if x < avg:
				l_cnt += 1
	# Сохранение значений
	av.append(avg)
	l.append(l_cnt)

# Блок вывода
print('Получившаяся матрица: ')
for i in range(len(matrix)):
	for el in matrix[i]:
		print('{:^8.2g}'.format(el), end='')
	print('{:^8.2g}'.format(av[i]), end='')
	print('{:^8.2g}'.format(l[i]))
