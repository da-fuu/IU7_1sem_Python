from file_io import start, print_file, get_size
from struct import calcsize, unpack, pack


def count_threes(file, length, num_size):
    count = 0
    for i in range(length):
        num = unpack('<l', file.read(num_size))[0]
        if num % 3 == 0:
            count += 1
    return count


def double_threes(filename, length, num_size):
    with open(filename, 'r+b') as file:
        threes = count_threes(file, length, num_size)
        for i in range(threes):
            file.write(pack('<l', 0))
        pos = (length + threes - 1) * num_size
        for ind in range(length - 1, -1, -1):
            file.seek(ind * num_size)
            num = unpack('<l', file.read(num_size))[0]
            if num % 3 == 0:
                file.seek(pos)
                file.write(pack('<l', num * 2))
                pos -= num_size
            file.seek(pos)
            file.write(pack('<l', num))
            pos -= num_size


def main():
    filename = start()
    size = calcsize('<l')
    nums = get_size(filename) // size
    double_threes(filename, nums, size)
    print_file(filename)


if __name__ == '__main__':
    main()
