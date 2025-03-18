# Удаление записи

from struct import calcsize
from utils import get_size


def main(filename, structure):
    # Ввод номера удаляемой записи
    entry_size = calcsize(structure)
    lines = get_size(filename) // entry_size
    line = input('Введите номер удаляемой записи: ').strip()
    while not (line.isdigit() and 0 < int(line) <= lines):
        line = input('Введите корректный номер удаляемой записи: ').strip()
    line = int(line)

    # Удаление записи
    with open(filename, 'r+b') as file:
        file.seek((line - 1) * entry_size)
        while line < lines:
            file.seek(line*entry_size)
            entry = file.read(entry_size)
            file.seek((line-1)*entry_size)
            file.write(entry)
            line += 1
        file.truncate()
