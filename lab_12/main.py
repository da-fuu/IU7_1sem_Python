# Жаринов Михаил ИУ7-12Б Лабораторная работа №12
# Текстовый процессор

from align import left, right, width
import delete_word
import replace_word
import eval_num
import delete_sentence


def print_menu():
    print('0. Завершить программу.')
    print('1. Выровнять текст по левому краю.')
    print('2. Выровнять текст по правому краю.')
    print('3. Выровнять текст по ширине.')
    print('4. Удалить все вхождения заданного слова.')
    print('5. Заменить одно слова другим во всём тексте.')
    print('6. Вычислить арифметические выражение(сложение и вычитание).')
    print('7. Найти и удалить предложение, содержащее слово с максимальным количеством согласных букв.')


def main():
    text = [
        'Использование меню предполагает, что пользователь может самостоятельно и',
        'многократно 13.-.1 13.1+12 выбирать, какой из функций, заложенных в программе, ему',
        'воспользоваться. Это означает13-45, 13 -45 - что пронумерованный список всех действий',
        'должен быть выведен на экран (в) виде меню, 10-11- 13- а также должно быть оформлено',
        'приглашение ввода, предлагающее пользователю выбрать какой-либо пункт. ff',
        '-10+1 -4=6 7=8J 9 -4+*6 10 +6 - 10 -6 10- - 6.'
    ]
    operations = [
        left,
        right,
        width,
        delete_word.main,
        replace_word.main,
        eval_num.main,
        delete_sentence.main
    ]
    aligned_type = 0
    while True:
        for line in text:
            print(line)
        print('-'*(max([len(line) for line in text])+1))
        print_menu()
        input_choose = input('Введите число от 0 до 7: ').strip()
        if not (input_choose.isdigit() and 0 <= int(input_choose) <= 7):
            print('Введите корректное число!')
            continue
        choose = int(input_choose)
        if choose == 0:
            return
        aligned_type = operations[choose-1](text, aligned_type)
        print('-'*(max([len(line) for line in text])+1))


if __name__ == '__main__':
    main()
