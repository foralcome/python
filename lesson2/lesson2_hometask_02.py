def lesson2_hometask02():
    print('2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')

    number_str = input('введите число: ')
    if not number_str.isnumeric() or int(number_str) <= 0:
        print('введённая строка не является числом!')
        return
    number = int(number_str)

    res = []
    for n in range(1, number + 1):
        value = 1
        for x in range(1, n + 1):
            value *= x
        res.append(value)

    print(res)
