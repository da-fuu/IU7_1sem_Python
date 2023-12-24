# Жаринов Михаил Андреевич ИУ7-12Б Лабораторная работа №3

import math

# Блок ввода
xa, ya = map(float, input('Введите координаты первой точки через пробел: ').split())
xb, yb = map(float, input('Введите координаты второй точки через пробел: ').split())
xc, yc = map(float, input('Введите координаты третьей точки через пробел: ').split())
xd, yd = map(float, input('Введите координаты четвертой точки через пробел: ').split())
xe, ye = map(float, input('Введите координаты пятой точки через пробел: ').split())

# Блок вычислений
# Расчет длин сторон
ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
# Расчет площади
abc_half_perimeter = (ab + bc + ac) / 2
abc_area = (abc_half_perimeter * (abc_half_perimeter - ab) * (abc_half_perimeter - bc) * (
        abc_half_perimeter - ac)) ** 0.5
h = 2 * abc_area / max(ab, ac, bc)
# Расчет максимального угла
max_len = max(ab, ac, bc)
min_len = min(ab, ac, bc)
med_len = ab + bc + ac - min_len - max_len

max_angle = math.acos((med_len ** 2 + min_len ** 2 - max_len ** 2) / (2 * med_len * min_len))

# Расчет площадей с третьей точкой
ad = ((xa - xd) ** 2 + (ya - yd) ** 2) ** 0.5
bd = ((xd - xb) ** 2 + (yd - yb) ** 2) ** 0.5
cd = ((xd - xc) ** 2 + (yd - yc) ** 2) ** 0.5
abd_half_perimeter = (ab + bd + ad) / 2
abd_area = (abd_half_perimeter * (abd_half_perimeter - ab) * (abd_half_perimeter - bd) * (
        abd_half_perimeter - ad)) ** 0.5
acd_half_perimeter = (ad + cd + ac) / 2
acd_area = (acd_half_perimeter * (acd_half_perimeter - ad) * (acd_half_perimeter - cd) * (
        acd_half_perimeter - ac)) ** 0.5
bcd_half_perimeter = (bd + bc + cd) / 2
bcd_area = (bcd_half_perimeter * (bcd_half_perimeter - bd) * (bcd_half_perimeter - bc) * (
        bcd_half_perimeter - cd)) ** 0.5
# Сортировка точек
if xe < xd:
    xd, xe = xe, xd
    yd, ye = ye, yd
if xb < xa:
    xb, xa = xa, xb
    yb, ya = ya, yb
if xc < xb:
    xc, xb = xb, xc
    yc, yb = yb, xc
# Расчет уравнений прямых
if abs(xa - xb) < 10 ** -6:
    kab = None
    bab = xa
else:
    kab = (yb - ya) / (xb - xa)
    bab = ya - kab * xa

if abs(xa - xc) < 10 ** -6:
    kac = None
    bac = xa
else:
    kac = (yc - ya) / (xc - xa)
    bac = ya - kac * xa

if abs(xb - xc) < 10 ** -6:
    kbc = None
    bbc = xb
else:
    kbc = (yc - yb) / (xc - xb)
    bbc = yb - kbc * xb

if abs(xe - xd) < 10 ** -6:
    kde = None
    bde = xd
else:
    kde = (ye - yd) / (xe - xd)
    bde = yd - kde * xd

intersect = False
# Проверка пересечений
if kde is not None:
    if kab is not None:
        if abs(kde - kab) > 10 ** -6:
            x = (bab - bde) / (kde - kab)
            if max(xd, xa) < x < min(xe, xb):
                intersect = True
    else:
        if ya - 10 ** -6 <= bab * kde + bde <= yb + 10 ** -6 and xd - 10 ** -6 <= bab <= xe + 10 ** -6:
            intersect = True

    if kac is not None:
        if abs(kde - kac) > 10 ** -6:
            x = (bac - bde) / (kde - kac)
            if max(xd, xa) < x < min(xe, xc):
                intersect = True
    else:
        if ya - 10 ** -6 <= bac * kde + bde <= yc + 10 ** -6 and xd - 10 ** -6 <= bac <= xe + 10 ** -6:
            intersect = True

    if kbc is not None:
        if abs(kde - kbc) > 10 ** -6:
            x = (bbc - bde) / (kde - kbc)
            if max(xd, xb) < x < min(xe, xc):
                intersect = True
    else:
        if yb - 10 ** -6 <= bbc * kde + bde <= yc + 10 ** -6 and xd - 10 ** -6 <= bbc <= xe + 10 ** -6:
            intersect = True
else:
    if kab is not None:
        if yd - 10 ** -6 <= bde * kab + bab <= ye + 10 ** -6 and xa - 10 ** -6 <= bde <= xb + 10 ** -6:
            intersect = True
    if kac is not None:
        if yd - 10 ** -6 <= bde * kac + bac <= ye + 10 ** -6 and xa - 10 ** -6 <= bde <= xc + 10 ** -6:
            intersect = True
    if kbc is not None:
        if yd - 10 ** -6 <= bde * kbc + bbc <= ye + 10 ** -6 and xb - 10 ** -6 <= bde <= xc + 10 ** -6:
            intersect = True

# Блок вывода
print('Длины сторон: {:.6g}, {:.6g}, {:.6g}'.format(ab, ac, bc))
if abc_area < 10 ** -6:
    print('Треугольник вырожденный')
else:
    print('Длина высоты: {:.6g}'.format(h))
    if max_angle > (math.pi / 2 + 10 ** -6):
        print('Треугольник тупоугольный')
    else:
        print('Треугольник не тупоугольный')

if acd_area + abd_area + bcd_area - abc_area < 10 ** -6:
    print('Точка внутри треугольника')
else:
    print('Точка снаружи треугольника')

if intersect:
    print('Отрезок пересекает треугольник')
else:
    print('Отрезок не пересекает треугольник')
