# Добавление после удвоенного числа после чисел кратных 3

# Подключение модулей
from file_io import start, print_file, get_size, fmt
from struct import calcsize, unpack, pack


# Подсчет чисел кратных 3
def count_threes(file, length, num_size):
    count = 0
    for i in range(length):
        num = unpack(fmt, file.read(num_size))[0]
        if num % 3 == 0:
            count += 1
    return count


# Добавление удвоенных чисел
def double_threes(filename, length, num_size):
    with open(filename, 'r+b') as file:
        # Увеличение файла
        threes = count_threes(file, length, num_size)
        for i in range(threes):
            file.write(pack(fmt, 0))

        # Запись в файл с конца, при необходимости добавляя удвоенное
        pos = (length + threes - 1) * num_size
        for ind in range(length - 1, -1, -1):
            file.seek(ind * num_size)
            num = unpack(fmt, file.read(num_size))[0]
            if num % 3 == 0:
                file.seek(pos)
                file.write(pack(fmt, num * 2))
                pos -= num_size
            file.seek(pos)
            file.write(pack(fmt, num))
            pos -= num_size


# Основная функция
def main():
    filename = start()
    size = calcsize(fmt)
    nums = get_size(filename) // size
    double_threes(filename, nums, size)
    print_file(filename)


if __name__ == '__main__':
    main()
