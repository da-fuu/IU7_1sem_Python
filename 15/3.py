from file_io import start, print_file, get_size
from struct import calcsize, unpack, pack


def read_file(file, ind, num_size):
    file.seek(ind * num_size)
    return unpack('<2l', file.read(num_size * 2))


def write_file(file, ind, num1, num2, num_size):
    file.seek(ind * num_size)
    file.write(pack('<2l', num1, num2))


def shaker_sort(filename, length, num_size):
    with open(filename, 'r+b') as file:
        for i in range(length - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                num = read_file(file, j, num_size)
                if num[1] < num[0]:
                    write_file(file, j, num[1], num[0], num_size)

            for j in range(i):
                num = read_file(file, j, num_size)
                if num[1] < num[0]:
                    write_file(file, j, num[1], num[0], num_size)


def main():
    filename = start()
    size = calcsize('<l')
    nums = get_size(filename) // size
    shaker_sort(filename, nums, size)
    print_file(filename)


if __name__ == '__main__':
    main()
