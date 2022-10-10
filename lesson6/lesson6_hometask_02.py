import random

def get_list_multiplicity_20_or_21_by_comprehension(ls):
    return [v for v in ls if v % 20 == 0 or v % 21 == 0]


def lesson6_hometask02():
    print(
        '2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.')

    n_str = input('введите количество элементов списка: ')
    if not n_str.isdigit() or int(n_str) <= 20:
        print('введённая строка должна быть числом (>20)!')
        return
    n = int(n_str)

    ls = list(range(20, n + 1))
    print(ls)

    print('результат:', get_list_multiplicity_20_or_21_by_comprehension(ls))
