def main(text, _=None):
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
    return 0
