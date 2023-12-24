def left(text, _=None):
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
    return 0


def right(text, _=None):
    left(text)
    max_len = len(max(text, key=len))
    for i in range(len(text)):
        text[i] = ' ' * (max_len - len(text[i])) + text[i]
    return 1


def align_line_width(line, length):
    words = line.split()
    if len(words) == 0:
        return ' ' * length
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


def width(text, _=None):
    left(text)
    max_len = len(max(text, key=len))
    for i in range(len(text)):
        text[i] = align_line_width(text[i], max_len)
    return 2


def main(text, align_type):
    align_methods = [
        left,
        right,
        width
    ]
    return align_methods[align_type](text)
