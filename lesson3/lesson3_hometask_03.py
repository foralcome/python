def convert_number_base_10_to_2(number):
    n = int(number)
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(number)
    return b

def lesson3_hometask03():
    print('3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.\
Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.')

    number_str = input('введите число: ')
    if not number_str.isnumeric() or int(number_str) <= 0:
        print('введённая строка не является числом!')
        return
    number = int(number_str)

    print(f'двоичное представление числа {number_str}:', convert_number_base_10_to_2(number))
