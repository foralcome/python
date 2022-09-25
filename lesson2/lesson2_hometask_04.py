def create_list(size):
    return list(range(-size, size + 1))


def print_list(l):
    print(l)


def lesson2_hometask04():
    print(
        '* 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах)')

    number_str = input('введите количество элементов списка: ')
    if not number_str.isnumeric() or int(number_str) <= 0:
        print('количество элементов должно быть больше 0!')
        return
    number = int(number_str)
    l = create_list(number)
    print_list(l)
    size_list = number * 2 + 1

    pos1_str = input('введите первую позицию: ')
    if not pos1_str.isnumeric() or int(pos1_str) > size_list or int(pos1_str) <= 0:
        print(f'позиция 1-го элемента должна быть в диапазоне [1,{size_list}]!')
        return
    pos1 = int(pos1_str)
    print('значение списка с', pos1, 'позицией равна', l[pos1 - 1])

    pos2_str = input('введите вторую позицию: ')
    if not pos2_str.isnumeric() or int(pos2_str) > size_list or int(pos2_str) <= 0:
        print(f'позиция 1-го элемента должна быть в диапазоне [1,{size_list}]!')
        return
    pos2 = int(pos2_str)
    print('значение списка с', pos2, 'позицией равна', l[pos2 - 1])

    print(' произведение значений элементов позиции', pos1, 'и', pos2, 'равна', str(l[pos1 - 1] * l[pos2 - 1]))
