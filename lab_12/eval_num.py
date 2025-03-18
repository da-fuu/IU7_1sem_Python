from align import main as align


def check_num(word):
    return all(s in '0123456789+-.' for s in word) and word[0] not in '-+' and word[-1] not in '+-' \
           and '--' not in word and '+-' not in word and '-+' not in word and '..' not in word


def type_get(word):
    if all(s in '0123456789.' for s in word):
        return 'n'
    if len(word) == 1:
        if word in '-+':
            return 'o'
        return '?'
    if len(word) == 2:
        if word[0] in '-+' and word[1].isdigit():
            return 'on'
        if word[1] in '-+' and word[0].isdigit():
            return 'no'
        if word[1] == '.' and word[0].isdigit():
            return 'n'
        if word[0] == '.' and word[1].isdigit():
            return 'n'
        return '?'
    if word[0] in '+-' and word[-1] in '+-':
        if check_num(word[1:-1]):
            return 'o'
        else:
            return '?'
    if word[0] in '+-':
        if check_num(word[1:]):
            return 'on'
        else:
            return '?'
    if word[-1] in '+-':
        if check_num(word[:-1]):
            return 'no'
        else:
            return '?'
    if check_num(word):
        return 'n'
    return '?'


def glue(line):
    words = line.split()
    last_word = type_get(words[0])
    new_line = words[0]
    last_len = len(new_line)
    for word in words[1:]:
        new_word = type_get(word)
        if last_word[-1] == 'n' and new_word[0] == 'o' or new_word[0] == 'n' and last_word[-1] == 'o':
            new_line += word
            last_word = new_word
            last_len = len(word)
            continue
        if last_word[-1] == 'o':
            new_line = new_line[:-last_len] + ' ' + new_line[-last_len:]
        new_line += ' ' + word
        last_word = new_word
        last_len = len(word)
    return new_line


def eval_n(word):
    words = word.replace('+', ' + ').replace('-', ' - ').split()
    res = float(words[0])
    for i in range(1, len(words), 2):
        if words[i] == '-':
            res -= float(words[i+1])
        else:
            res += float(words[i+1])
    return str(res)


def main(text, align_type):
    for j in range(len(text)):
        if not text[j]:
            continue
        line = glue(text[j])
        words = line.split()
        for i, word in enumerate(words):
            if word[0] in '-+':
                word = '0' + word
            end = ''
            if word[-1] in ',.:;':
                end = word[-1]
                word = word[:-1]

            if check_num(word):
                words[i] = eval_n(word) + end
        text[j] = ' '.join(words)
    return align(text, align_type)
