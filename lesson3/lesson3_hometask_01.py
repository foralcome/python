import random


def get_random_list_integer(size, min=0, max=99):
    ls = []
    for i in range(size):
        ls.append(random.randint(min, max))
    return ls


def print_list_integer(list_values):
    print(list_values)


def get_sum_values_on_even_position(list_values):
    sum = 0
    for i in range(1, len(list_values), 2):
        sum += list_values[i]
    return sum


def get_sum_values(list_values):
    return sum(list_values)


def get_values_on_even_position(list_values):
    list_even = []
    for i in range(1, len(list_values), 2):
        list_even.append(list_values[i])
    return list_even


def get_values_on_not_even_position(list_values):
    list_not_even = []
    for i in range(0, len(list_values), 2):
        list_not_even.append(list_values[i])
    return list_not_even


def lesson3_hometask01():
    print('1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. \
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).')

    size_str = input('введите количество элементов списка: ')
    if not size_str.isdigit():
        print('введённая строка должна быть числом (>0)!')
        return
    size = int(size_str)

    ls = get_random_list_integer(size)
    print_list_integer(ls)

    even_values = get_values_on_even_position(ls)
    print("сумма чётных чисел", "+".join(map(str, even_values)), '=', get_sum_values(even_values))
    not_even_values = get_values_on_not_even_position(ls)
    print("сумма НЕчётных чисел", "+".join(map(str, not_even_values)), '=', get_sum_values(ls))
