from struct import pack
from utils import ask_for_entry


def main(filename, structure):
    entry_ind = input('Введите количество строк: ').strip()
    while not (entry_ind.isdigit() and int(entry_ind) > 0):
        entry_ind = input('Введите корректное количество строк: ').strip()
    entry_ind = int(entry_ind)
    with open(filename, 'wb') as file:
        for i in range(1, entry_ind + 1):
            entry = ask_for_entry(i)
            file.write(pack(structure, *entry))
