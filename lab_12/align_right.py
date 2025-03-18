def main(text, _=None):
    max_len = len(max(text, key=len))
    for i in range(len(text)):
        text[i] = ' ' * (max_len - len(text[i])) + text[i]
    return 1
