from align import main as align


def main(text, align_type):
    del_word = input('Введите заменяемое слово: ').strip()
    while ' ' in del_word or not del_word:
        del_word = input('Введите строго одно заменяемое слово: ').strip()
    new_word = input('Введите новое слово: ').strip()
    while ' ' in new_word or not new_word:
        new_word = input('Введите строго одно новое слово: ').strip()
    for i in range(len(text)):
        words = text[i].split()
        for j, word in enumerate(words):
            if word == del_word:
                words[j] = new_word
            elif len(del_word) + 1 == len(word) and word[:-1] == del_word and word[-1] in ',.;:-':
                words[j] = new_word + word[-1]
        text[i] = ' '.join(words)
    return align(text, align_type)
