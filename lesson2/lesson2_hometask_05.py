import random

def lesson2_hometask05():
    print('** 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random')

    size_str = input('введите размер списка: ')
    if not size_str.isnumeric() or int(size_str) <= 0:
        print('количество элементов должно быть больше 0!')
        return
    size = int(size_str)
    l = list(range(size))
    print(l)

    count_replace_str = input('укажите количество перестановок: ')
    if not count_replace_str.isnumeric() or int(count_replace_str) <= 0:
        print('количество перестановок быть больше 0!')
        return
    count_replace = int(count_replace_str)

    while count_replace > 0:
        index_num1 = random.randint(0, size - 1)
        index_num2 = random.randint(0, size - 1)
        if index_num1 == index_num2:
            continue

        l[index_num1], l[index_num2] = l[index_num2], l[index_num1]
        count_replace -= 1
    print(l)
