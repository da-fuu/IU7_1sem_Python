# Жаринов Михаил ИУ7-12Б Лабораторная работа №10
# Расчет интеграла функции
from math import log, exp


# Данная функция
def f(x):
    return x ** 2


# Первоообразная функции
def f_antiderivative(x):
    return x ** 3 / 3


# Проверка строки на десятичную дробь
def is_decimal(s):
    if s[0] == '-':
        s = s[1:]
    if s.count('.') == 1:
        return all([i.isdigit() for i in s.split('.')])
    if '.' in s:
        return 0
    return s.isdigit()


# Проверка строки на действительное число
def is_real(s):
    if not s:
        return 0
    if s.count('e') == 1:
        ex = s.split('e')[1]
        if ex[0] == '-':
            return is_decimal(s.split('e')[0]) and ex[1:].isdigit()
        if '-' in ex:
            return 0
        return is_decimal(s.split('e')[0]) and ex.isdigit()
    if 'e' in s:
        return 0
    return is_decimal(s)


# Расчет интеграла методом левых прямоугольников
def left_rect(n, start, stop):
    h = (stop - start) / n
    s = 0
    for i in range(0, n):
        s += f(start + h * i)
    s *= h
    return s


# Расчет интеграла методом 3/8
def three_eights(n, start, stop):
    h = (stop - start) / n
    s = 0
    for i in range(0, n - 2):
        s += f(start + i * h) + 3 * f(start + (i + 1) * h) + 3 * f(start + (i + 2) * h) + f(start + (i + 3) * h)
    s /= 8
    s *= h
    return s


# Подбор числа делений для получения интеграла с необходимой точностью
def get_best_integral(method, eps, start, stop):
    n = 1
    while abs(method(n, start, stop) - method(2 * n, start, stop)) > eps:
        n *= 2
    return n, method(n, start, stop)


# Блок ввода
input_start = input('Введите начало отрезка: ').strip()
input_stop = input('Введите конец отрезка: ').strip()
input_n1 = input('Введите первое количество делений: ').strip()
input_n2 = input('Введите второе количество делений: ').strip()
# Проверка ввода
if is_real(input_start) and is_real(input_stop) and input_n1.isdigit() and input_n2.isdigit():
    start = float(input_start)
    stop = float(input_stop)
    n = [int(input_n1), int(input_n2)]
    if stop > start and n[0] > 0 and n[1] > 0:
        # Расчет интегралов
        integral_first = [left_rect(n[0], start, stop), left_rect(n[1], start, stop)]
        integral_second = [three_eights(n[0], start, stop), three_eights(n[1], start, stop)]
        # Расчет точного интеграла
        true_integral = f_antiderivative(stop) - f_antiderivative(start)
        # Расчет погрешностей
        abs_diffs = [abs(x - true_integral) for x in (integral_first + integral_second)]
        rel_diffs = [x / true_integral for x in abs_diffs]
        # Вывод значений интегралов
        print(' ' * 10 + 'N1' + ' ' * 10 + 'N2')
        print('Метод 1  {:< 12.7g}{:< 12.7g}'.format(*integral_first))
        print('Метод 2  {:< 12.7g}{:< 12.7g}'.format(*integral_second))
        print('Настоящее значение интеграла: {:.7g}'.format(true_integral))
        # Вывод погрешностей
        for i in range(4):
            print('Абсолютная погрешность метода {} при числе делений {:.7g}: {:.7g}'
                  .format(i // 2 + 1, n[i % 2], abs_diffs[i]))
            print('Относительная: {:.7g}'.format(rel_diffs[i]))
        # Ввод требуемой точности
        input_e = input('Введите eps: ').strip()
        if is_real(input_e):
            # Расчет интеграла лучшим методом
            if abs_diffs.index(min(abs_diffs)) < 2:
                good_n, good_integral = get_best_integral(left_rect, float(input_e), start, stop)
                print('Лучший метод - метод левых прямоугольников')
            else:
                good_n, good_integral = get_best_integral(three_eights, float(input_e), start, stop)
                print('Лучший метод - метод 3/8')
            # Вывод приближенного значения
            print('Приближенное значение интеграла: {:.7g}'.format(good_integral))
            print('Необходимое количество делений: {:.7g}'.format(good_n))
        else:
            print('Введено некорректное значение!')
    else:
        print('Введены некорректные значения!')
else:
    print('Введены некорректные значения!')
