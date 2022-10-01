import random


def get_random_list_double(size, min=0, max=10, size_fraction=0):
    ls = []
    for i in range(size):
        if size_fraction == 0:
            ls.append(random.uniform(min, max))
        else:
            ls.append(round(random.uniform(min, max), size_fraction))
    return ls


def get_min_max_tuple(l):
    return min(l), max(l)


def get_fraction_number(n):
    return n % 1


def get_min_max_fraction_tuple(l):
    return min(map(get_fraction_number, l)), max(map(get_fraction_number, l))


def lesson3_hometask04():
    print('* 4.Задайте список из произвольных вещественных чисел, количество задаёт пользователь.\
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')

    size_str = input('введите количество элементов списка: ')
    if not size_str.isdigit() or int(size_str) <= 0:
        print('введённая строка должна быть числом (>0)!')
        return
    size = int(size_str)

    count_fraction_str = input('введите количество знаков после запятой: ')
    if not count_fraction_str.isdigit() or int(count_fraction_str) < 1:
        print('введённая строка должна быть числом (>1)!')
        return
    count_fraction = int(count_fraction_str)

    ls = get_random_list_double(size, size_fraction=count_fraction)
    print(ls)

    min, max = get_min_max_fraction_tuple(ls)
    min = round(min, count_fraction)
    max = round(max, count_fraction)
    print(f"Минимальное значение {min}, максимальное значение {max}")

    difference_fraction_max_min = round(max - min, count_fraction)
    print(f"Разница дробной части {difference_fraction_max_min}")
