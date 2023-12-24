# Жаринов Михаил Андреевич ИУ7-12Б Лабораторная №4
# Программа выводит таблицу значений и график функции

# Блок ввода
start, stop, step = \
    map(float, input('Введите начало, конец отрезка и шаг через пробел: ')
        .split())
# start, step, stop = 1.4, 0.025, 2.2

# Обратока неверного ввода
if (stop - start) > 10 ** -8 and step > 10 ** -8:
    points = int(input('Введите количество засечек от 4 до 8: '))

    # Вывод шапки таблицы
    print('-' * 30)
    print('|  {:^11} | {:^11} |'.format('y', 'd'))
    print('|', '-' * 28, '|', sep='')

    # Вывод строк таблицы
    iters = int((stop - start) / step) + 1
    min_d = max_d = start ** 5 - 7.9 * start ** 4 + 24.46 * start ** 3 \
                    - 37.074 * start ** 2 + 27.512 * start - 8.0042
    y_max = start
    for i in range(iters):
        y = round(start + step * i, 13)
        d = y ** 5 - 7.9 * y ** 4 + 24.46 * y ** 3 - 37.074 * y ** 2 \
            + 27.512 * y - 8.0042
        print('|  {:<11.5g} | {:<11.5g} |'.format(y, d))

        # Обновление макс и мин значений
        if d > max_d:
            y_max = y
            max_d = d
        min_d = min(min_d, d)

    # Вывод конца таблицы
    print('-' * 30)
    print('Максимальное значение функции: {:.5g}, достигается при у={:.5g}'
          .format(max_d, y_max))

    # Проверка на верность ввода
    if 4 <= points <= 8:

        # Вывод шапки графика
        print('  f1', ' ' * 6, end='|')
        pad = round((95 - points * 11) / (points - 1))
        for i in range(points):
            if i == 0:
                print('{:<11.5g}'.format(i * ((max_d - min_d)
                                              / (points - 1)) + min_d),
                      end=' ' * (pad if points != 6 else pad - 1))
            elif i == points - 1:
                print('{:>11.5g}'
                      .format(i * ((max_d - min_d)
                                   / (points - 1)) + min_d), end='|\n')
            else:
                print('{:^11.5g}'
                      .format(i * ((max_d - min_d)
                                   / (points - 1)) + min_d), end=' ' * pad)
        print('-' * 11, '|', '-' * 95, '|', sep='')

        # Вывод строчки графика
        for i in range(iters):
            y = round(start + step * i, 13)
            d = y ** 5 - 7.9 * y ** 4 + 24.46 * y ** 3 \
                - 37.074 * y ** 2 + 27.512 * y - 8.0042

            index = round((d - min_d) / (max_d - min_d) * 94)
            if min_d - 10 ** -6 <= 0 <= max_d + 10 ** -6:
                ind_zero = round((-min_d) / (max_d - min_d) * 94)
                if ind_zero < index:
                    print('{:<11.5g}|'.format(y), ind_zero * ' ', '|',
                          (index - ind_zero - 1) * ' ',
                          '*', (94 - index) * ' ', '|', sep='')
                elif ind_zero > index:
                    print('{:<11.5g}|'.format(y), index * ' ', '*',
                          (ind_zero - index - 1) * ' ', '|',
                          (94 - ind_zero) * ' ', '|', sep='')
                else:
                    print('{:<11.5g}|'.format(y), index * ' ', '*',
                          (94 - index) * ' ', '|', sep='')
            else:
                print('{:<11.5g}|'.format(y), index * ' ', '*',
                      (94 - index) * ' ', '|', sep='')

    else:
        print('Введено неверное количество засечек!')

else:
    print('Введены неверные данные!')
