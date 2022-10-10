import random


def get_random_list_integer(size, min=0, max=99):
    ls = []
    for i in range(size):
        ls.append(random.randint(min, max))
    return ls


def get_list_by_comprehension(ls):
    return [ls[i] for i in range(1, len(ls)) if ls[i] > ls[i - 1]]


def lesson6_hometask01():
    print(
        '1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.')

    size_str = input('введите количество элементов списка: ')
    if not size_str.isdigit():
        print('введённая строка должна быть числом (>0)!')
        return
    size = int(size_str)

    ls = get_random_list_integer(size, 1, 10)
    print(ls)

    print('результат:', get_list_by_comprehension(ls))
