def get_size(filename):
    with open(filename, 'rb') as file:
        file.seek(0, 2)
        size = file.tell()
        return size