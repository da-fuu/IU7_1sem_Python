from file_io import start, print_file, get_size
from struct import calcsize, unpack, pack


def delete_even(filename, length, num_size):
    with open(filename, 'r+b') as file:
        pos = 0
        for ind in range(0, length):
            file.seek(ind * num_size)
            num = unpack('<l', file.read(num_size))[0]
            if num % 2 != 0:
                file.seek(pos)
                file.write(pack('<l', num))
                pos += num_size
        file.truncate(pos)


def main():
    filename = start()
    size = calcsize('<l')
    nums = get_size(filename) // size
    delete_even(filename, nums, size)
    print_file(filename)


if __name__ == '__main__':
    main()
