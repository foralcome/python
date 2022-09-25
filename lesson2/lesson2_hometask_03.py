def lesson2_hometask03():
    print('3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.')

    number_str = input('введите число: ')
    if not number_str.isnumeric() or int(number_str) <= 0:
        print('введённая строка не является числом!')
        return
    number = int(number_str)

    sum = 0
    res = list()
    for n in range(1, number + 1):
        value = round((1 + 1 / n) ** n)
        sum += value
        res.append(value)

    print(res)
    print('сумма числе равна:', sum)
