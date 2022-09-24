def lesson1_hometask01():
    print(
        'Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')

    number = int(input('введите цифру дня недели (от 1 до 7): '))
    if number < 1 or number > 7:
        print('error: incorrect number of week!')
    elif number >= 1 and number <= 5:
        print('Work day!')
    else:
        print('Weekend!')
