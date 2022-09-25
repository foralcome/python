def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def lesson2_hometask01():
    print('1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')

    number_str = input('введите вещественное число: ')
    if not isfloat(number_str):
        print('введённая строка не является числом!')
        return

    sum = 0
    print('---------------------------------------------')
    print('вариант решения 1 - обход по строке float')
    for i in range(len(number_str)):
        if number_str[i].isnumeric():
            sum += int(number_str[i])
    print('сумма цифр числа', number_str, 'равна:', sum)

    print('-----------------------------------------------------------')
    sum = 0
    print('вариант решения 2 - обход по предобработанной строке float')
    number_str_modify = number_str.replace('-', '')
    number_str_modify = number_str_modify.replace('.', '')
    for i in range(len(number_str_modify)):
        sum += int(number_str_modify[i])
    print('сумма цифр числа', number_str, 'равна:', sum)

    print('---------------------------------------------------------')
    print('вариант решения 3 - обрабатываем вещественное число float')
    number = float(number_str)
    if number < 0:
        number *= -1

    integer_of_number = int(number)
    print('целая честь числа:', integer_of_number)
    fraction_of_number = int(number % 1 * 10 ** 5)
    print('дробная честь числа:', number % 1)

    fraction_sum = 0
    calc_number = fraction_of_number
    while calc_number > 0:
        fraction_sum += calc_number % 10
        calc_number //= 10
    print('сумма чисел дробной части:', fraction_sum)

    integer_sum = 0
    calc_number = integer_of_number
    while calc_number > 0:
        integer_sum += calc_number % 10
        calc_number //= 10
    print('сумма чисел целой части:', integer_sum)

    sum = integer_sum + fraction_sum
    print('сумма цифр числа', number_str, 'равна:', sum)
