import random


def get_random_list_integer(size, min=0, max=99):
    ls = []
    for i in range(size):
        ls.append(random.randint(min, max))
    return ls


def get_no_repeat_values_by_set(numbers):
    unique = list(set(numbers))
    no_repeat = []
    for i in range(len(unique)):
        i_find = numbers.index(unique[i])
        try:
            numbers.index(unique[i], i_find + 1)
        except IndexError:
            continue
        except ValueError:
            no_repeat.append(unique[i])
    return no_repeat


def get_no_repeat_values_by_dict(numbers):
    counter = {}
    for elem in numbers:
        counter[elem] = counter.get(elem, 0) + 1

    no_repeat = []
    for number in counter.keys():
        if counter[number]==1:
            no_repeat.append(number)
    return no_repeat


def lesson4_hometask03():
    print(
        '3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.')

    size_str = input('введите количество элементов списка: ')
    if not size_str.isdigit():
        print('введённая строка должна быть числом (>0)!')
        return
    size = int(size_str)

    ls = get_random_list_integer(size, 1, 10)
    print(ls)

    print('уникальные значения:', set(ls))

    print('способ 1: используем множества')
    print('не повторяющиеся значения:', get_no_repeat_values_by_set(ls))
    print('способ 2: используем словари')
    print('не повторяющиеся значения:', get_no_repeat_values_by_dict(ls))
