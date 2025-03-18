# Удаление четных чисел из файла

# Подключение модулей
from file_io import start, print_file, get_size, fmt
from struct import calcsize, unpack, pack


# Удаление четных чисел
def delete_even(filename, length, num_size):
    with open(filename, 'r+b') as file:
        pos = 0
        for ind in range(0, length):
            file.seek(ind * num_size)
            num = unpack(fmt, file.read(num_size))[0]
            if num % 2 != 0:
                file.seek(pos)
                file.write(pack(fmt, num))
                pos += num_size
        file.truncate(pos)


# Основная функция
def main():
    filename = start()
    size = calcsize('<l')
    nums = get_size(filename) // size
    delete_even(filename, nums, size)
    print_file(filename)


if __name__ == '__main__':
    main()
