def factorization_number(n):
    fact_numbers = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            fact_numbers.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        fact_numbers.append(n)
    return fact_numbers


def show_algoritm_factorization_number(n, fact_numbers):
    calc_n = n
    for d in fact_numbers:
        print(f"{calc_n: >7.2f} / {d} = {calc_n / d: >7.2f}")
        calc_n /= d


def lesson4_hometask02():
    print('2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N')

    n_str = input('введите натуральное число N: ')
    if not n_str.isdigit() or int(n_str) == 0:
        print('введённая строка должна быть числом (>0)!')
        return
    n = int(n_str)

    fact_numbers = factorization_number(n)
    print(fact_numbers)
    show_algoritm_factorization_number(n, fact_numbers)
