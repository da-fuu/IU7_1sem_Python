from struct import calcsize, pack
from utils import ask_for_entry, get_size


def main(filename, structure):
    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    line = input('Введите номер вставляемой записи: ').strip()
    while not (line.isdigit() and 0 <= int(line) - 1 <= lines):
        line = input('Введите корректный номер вставляемой записи: ').strip()
    line = int(line)
    with open(filename, 'r+b') as file:
        for i in range(lines, line - 1, -1):
            file.seek(entry_size*(i - 1))
            entry = file.read(entry_size)
            file.write(entry)
        entry = ask_for_entry(line)
        file.seek(entry_size * (line - 1))
        file.write(pack(structure, *entry))
