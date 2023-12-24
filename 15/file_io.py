from struct import pack, calcsize, unpack


def check_filename(filename):
    try:
        with open(filename, 'wb'):
            return True
    except OSError:
        return False


def ask_for_number(ind):
    num = input('Введите {:}-ое число: '.format(ind)).strip()
    while not (num.isdigit() and 2**31 > int(num) >= -2**31):
        num = input('Введите корректное 32-битное {:}-ое число: '.format(ind)).strip()
    return int(num)


def initialize(filename):
    if not check_filename(filename):
        return False
    entry_num = input('Введите количество чисел: ').strip()
    while not (entry_num.isdigit() and int(entry_num) > 0):
        entry_num = input('Введите корректное количество чисел: ').strip()
    entry_num = int(entry_num)
    with open(filename, 'wb') as file:
        for i in range(1, entry_num + 1):
            entry = ask_for_number(i)
            file.write(pack('<L', entry))
    return True


def print_file(filename):
    with open(filename, 'rb') as file:
        size = calcsize('<L')
        file.seek(0, 2)
        nums = file.tell() // size
        file.seek(0)
        for i in range(nums):
            entry = file.read(size)
            entry = unpack('<L', entry)
            print(entry)
