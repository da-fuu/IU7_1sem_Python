from align import main as align


def count_sogl(word):
    counter = 0
    for ch in word:
        if ch in 'qwrtpsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтб':
            counter += 1
    return counter


def main(text, align_type):
    all_words = []
    for line in text:
        all_words.append(line.split())
    start_ind = [0, 0]
    abs_max_inds = [start_ind, [-1, -1]]
    abs_max = curr_max = -1

    for i, line in enumerate(all_words):
        for j, word in enumerate(line):
            letters = count_sogl(word)
            if letters > curr_max:
                curr_max = letters
            if word[-1] in '?!.':

                if curr_max > abs_max:
                    abs_max = curr_max
                    abs_max_inds = [start_ind, [i, j]]
                    curr_max = 0
                start_ind = [i, j+1]
                if j + 1 == len(line):
                    start_ind = [i+1, 0]
    if abs_max_inds[0][0] == abs_max_inds[1][0]:
        for _ in range(abs_max_inds[0][1], abs_max_inds[1][1]+1):
            print('Удаляемое предложение:')
            print(all_words[abs_max_inds[0][0]].pop(abs_max_inds[0][1]), end=' ')
        print()
    elif abs_max_inds[0][0] < abs_max_inds[1][0]:
        print('Удаляемое предложение:')
        for _ in range(abs_max_inds[0][1], len(all_words[abs_max_inds[0][0]])):
            print(all_words[abs_max_inds[0][0]].pop(abs_max_inds[0][1]), end=' ')
        print()
        if abs_max_inds[0][0] + 1 < abs_max_inds[1][0]:
            for i in range(abs_max_inds[0][0] + 1, abs_max_inds[1][0]):
                print(*all_words[i])
                all_words[i] = []
        for _ in range(0, abs_max_inds[1][1]+1):
            print(all_words[abs_max_inds[1][0]].pop(0), end=' ')
        print()
    else:
        print('Пустой текст!')
    for i in range(len(text)):
        text[i] = ' '.join(all_words[i])

    return align(text, align_type)

