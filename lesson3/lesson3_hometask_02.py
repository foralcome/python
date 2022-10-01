import random


def get_random_list_integer(size, min=0, max=99):
    ls = []
    for i in range(size):
        ls.append(random.randint(min, max))
    return ls


def print_list_integer(list_values):
    print(list_values)


def get_multiplication_values_pair_position(list_values):
    ls = [];
    i = 0
    j = len(list_values) - 1
    while i <= j:
        if i == j:
            ls.append(list_values[i])
        else:
            ls.append(list_values[i] * list_values[j])
        i += 1
        j -= 1
    return ls


def lesson3_hometask02():
    print('2. Напишите программу, которая найдёт произведение пар чисел списка.\
Парой считаем первый и последний элемент, второй и предпоследний и т.д.')

    size_str = input('введите количество элементов списка: ')
    if not size_str.isdigit():
        print('введённая строка должна быть числом (>0)!')
        return
    size = int(size_str)

    ls = get_random_list_integer(size, 1, 10)
    print_list_integer(ls)

    print(get_multiplication_values_pair_position(ls))
