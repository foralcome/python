import random


def generate_random_string_list(count):
    chars = ['а', 'б', 'в']
    ls = []
    for a in chars:
        for b in chars:
            for c in chars:
                if a == b or b == c or c == a:
                    continue
                ls.append(''.join([a, b, c]))
    return random.choices(ls, k=count)


def filter_string(s):
    if s != 'абв':
        return True
    return False


def lesson5_hometask01():
    print(
        '1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.')

    ls_before = generate_random_string_list(20)
    print(' '.join(ls_before))
    ls_after = list(filter(filter_string, ls_before))
    print(' '.join(ls_after))
