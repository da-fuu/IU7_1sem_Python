from align import main as align


def main(text, align_type):
    del_word = input('Введите удаляемое слово: ').strip()
    while ' ' in del_word or not del_word:
        del_word = input('Введите строго одно удаляемое слово: ').strip()
    for i in range(len(text)):
        words = text[i].split()
        for j, word in enumerate(words):
            if word == del_word:
                words[j] = None
            elif len(del_word) + 1 == len(word) and word[:-1] == del_word and word[-1] in ',.;:-':
                if j == 0:
                    if i == 0:
                        words[0] = None
                    else:
                        text[i-1] += word[-1]
                else:
                    words[j-1] += word[-1]
                words[j] = None
        while None in words:
            words.remove(None)
        text[i] = ' '.join(words)
    return align(text, align_type)

