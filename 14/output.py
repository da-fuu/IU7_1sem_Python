from struct import unpack, calcsize
from utils import get_size, print_head, print_entry


def main(filename, structure):
    print_head()
    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    with open(filename, 'rb') as file:
        for i in range(lines):
            entry = file.read(entry_size)
            entry = unpack(structure, entry)
            print_entry(entry)
