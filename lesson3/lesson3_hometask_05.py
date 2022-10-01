def nega_fibonacci(n):
    fib_numbers = [0, 1, 1]
    fib1, fib2 = 1, 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_numbers.append(fib2)

    neg_fib_numbers = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            neg_fib_numbers.append(fib_numbers[i])
        else:
            neg_fib_numbers.append((-1) * fib_numbers[i])
    return neg_fib_numbers[::-1] + fib_numbers


def fibonacci(n):
    fib_numbers = [0, 1, 1]
    fib1, fib2 = 1, 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_numbers.append(fib2)
    return fib_numbers


def print_fibonacci(fib_numbers):
    for i in range(len(fib_numbers)):
        print(i, end=', ')
    print()
    for v in fib_numbers:
        print(v, end=', ')
    print()


def lesson3_hometask05():
    print('** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')

    number_str = input('введите число: ')
    if not number_str.isnumeric() or int(number_str) <= 0:
        print('число должно быть больше 0!')
        return
    number = int(number_str)

    fib_numbers = nega_fibonacci(number)
    print_fibonacci(fib_numbers)
