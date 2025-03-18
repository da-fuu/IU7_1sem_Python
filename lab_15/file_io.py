# Общие функции работы с файлом

# Подключение модулей
from struct import pack, calcsize, unpack

# Формат числа
fmt = '<l'


# Получение размера файла
def get_size(filename):
    with open(filename, 'rb') as file:
        file.seek(0, 2)
        size = file.tell()
        return size


# Проверка пути файла
def check_filename(filename):
    try:
        with open(filename, 'wb'):
            return True
    except OSError:
        return False


# Ввод числа
def ask_for_number(ind):
    num = input('Введите {:}-ое число: '.format(ind)).strip()
    while not ((num[1:] if num[0] == '-' else num).isdigit() and 2**31 > int(num) >= -2**31):
        num = input('Введите корректное 32-битное {:}-ое число: '.format(ind)).strip()
    return int(num)


# Инициализация файла
def initialize(filename):
    entry_num = input('Введите количество чисел: ').strip()
    while not (entry_num.isdigit() and int(entry_num) > 0):
        entry_num = input('Введите корректное количество чисел: ').strip()
    entry_num = int(entry_num)
    with open(filename, 'wb') as file:
        for i in range(1, entry_num + 1):
            entry = ask_for_number(i)
            file.write(pack('<l', entry))


# Вывод всех чисел из файла
def print_file(filename):
    size = calcsize('<l')
    nums = get_size(filename) // size
    if nums == 0:
        print('Получившийся файл пуст')
        return
    with open(filename, 'rb') as file:
        print('Получившийся файл:')
        for i in range(nums):
            entry = file.read(size)
            entry = unpack('<l', entry)
            print(entry[0])


# Ввод пути файла и его инициализация
def start():
    filename = input('Введите путь файла: ').strip()
    while not check_filename(filename):
        filename = input('Введите корректный путь файла: ').strip()
    initialize(filename)
    return filename
