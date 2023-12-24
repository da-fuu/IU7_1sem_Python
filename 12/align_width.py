def align_line(line, length):
    words = line.split()
    if len(words) == 1:
        return ' ' * ((length - len(words[0])) // 2) + words[0]
    new_line = words.pop(0)
    length -= len(new_line)

    while words:
        total_spaces = length - sum([len(w) for w in words])
        spaces = total_spaces // len(words)
        new_word = ' ' * spaces + words.pop(0)
        length -= len(new_word)
        new_line += new_word
    return new_line


def main(text, _=None):
    max_len = len(max(text, key=len))
    for i in range(len(text)):
        text[i] = align_line(text[i], max_len)
    return 2
