from struct import unpack, calcsize
from utils import get_size


def main(filename, structure):
    print('|{:^15}|{:^11}|{:^9}'.format('Фамилия', 'Группа', 'Возраст'))
    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    with open(filename, 'rb') as file:
        for i in range(lines):
            entry = file.read(entry_size)
            entry = unpack(structure, entry)
            print('|{:^15}|{:^11}|{:^9}'.format(entry[0].decode().rstrip('\x00'), entry[1].decode().rstrip('\x00'), str(entry[2])))
