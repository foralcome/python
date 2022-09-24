def lesson1_hometask04():
    print(
        '4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')

    quarter = int(input('Укажите номер четверти: '))
    if quarter < 1 or quarter > 4:
        print('указане недействительный номер четверти!')
        return

    if quarter == 1:
        print('1 четверть: x > 0 and y > 0')
    if quarter == 2:
        print('2 четверть: x < 0 and y > 0')
    if quarter == 3:
        print('3 четверть: x < 0 and y < 0')
    if quarter == 4:
        print('4 четверть: x > 0 and y < 0')
