from struct import calcsize
from utils import ask_for_entry, get_size


def main(filename, structure):
    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    line = input('Введите номер вставляемой записи: ').strip()
    while not (line.isdigit() and 0 <= int(line) - 1 <= lines):
        line = input('Введите корректный номер вставляемой записи: ').strip()
    line = int(line)
    with open(filename, 'r+b') as file:
        for i in range(lines, line):
            file.seek()
        surname, group, age = ask_for_entry(line)

