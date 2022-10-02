from decimal import Decimal


def lesson4_hometask01():
    print('1. Вычислить число c заданной точностью d')

    number_str = input('Enter a real number: ')
    if not number_str.replace('-', '').isdigit():
        print('введённая строка должна быть числом!')
        return
    accuracy_str = input("Enter the required accuracy (format '0.0001'): ")

    print(Decimal(number_str) + Decimal(accuracy_str) - Decimal(accuracy_str))
