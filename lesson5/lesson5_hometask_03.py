import os, random


def print_rules(size):
    data_start = list(range(1, size ** 2 + 1))
    print_table(size, data_start)
    print(
        f'Правила:\n1) нумерация ячеек от 1 до {size ** 2}\n2) чтобы установить X или 0 в ячейку укажите её номер когда будет ваш ход.')
    print('...для продолжения нажмите на любую клавишу...')


def print_table(size, data):
    print('----' * (size + 1))
    for row in range(size):
        for col in range(size):
            print(f'  {data[row * size + col]}  ', end='')
            if col == size - 1:
                print()
        print('----' * (size + 1))


def set_player_settings(id_player, marker_player=''):
    print(f'Настройки игрока {id_player}')
    name_player = input('Введите ваше имя: ')

    if marker_player == '':
        marker_player = input('Выберите чем будете играть (введите X или 0): ')
        while len(marker_player) == 0 or (marker_player.lower() != 'x' and marker_player != '0'):
            marker_player = input('Выберите чем будете играть (введите X или 0): ')

    return (id_player, name_player, marker_player.upper())


def get_player_id_win(size, data, marker_player_1='X', marker_player_2='0', count_for_win=3):
    # проверяем горизонталь
    for row in range(size):
        marker_player_1_count = 0
        marker_player_2_count = 0
        for col in range(size):
            if data[row * size + col] == marker_player_1:
                marker_player_1_count += 1
            if data[row * size + col] == marker_player_2:
                marker_player_2_count += 1
        # print(f'проверка горизонтали {row}- Player1: {marker_player_1_count}')
        if marker_player_1_count == count_for_win:
            return 1
        # print(f'проверка горизонтали {row}- Player2: {marker_player_2_count}')
        if marker_player_2_count == count_for_win:
            return 2

    # проверяем вертикаль
    for col in range(size):
        marker_player_1_count = 0
        marker_player_2_count = 0
        for row in range(size):
            if data[row * size + col] == marker_player_1:
                marker_player_1_count += 1
            if data[row * size + col] == marker_player_2:
                marker_player_2_count += 1
        # print(f'проверка вертикали {col}- Player1: {marker_player_1_count}')
        if marker_player_1_count == count_for_win:
            return 1
        # print(f'проверка вертикали {col}- Player2: {marker_player_2_count}')
        if marker_player_2_count == count_for_win:
            return 2

    # проверяем главную диагональ
    marker_player_1_count = 0
    marker_player_2_count = 0
    for i in range(size):
        if data[i + i * size] == marker_player_1:
            marker_player_1_count += 1
        if data[i + i * size] == marker_player_2:
            marker_player_2_count += 1
        # print(f'проверка диагонали (ячейка) {i + i * size} маркет {marker_player_1} в ячейке {data[i + i * size]} - Player1: {marker_player_1_count}/{count_for_win}')
        if marker_player_1_count == count_for_win:
            return 1
        # print(f'проверка диагонали (ячейка) {i + i * size} маркет {marker_player_2} в ячейке {data[i + i * size]} - Player2: {marker_player_2_count}/{count_for_win}')
        if marker_player_2_count == count_for_win:
            return 2

    # проверяем диагональ
    marker_player_1_count = 0
    marker_player_2_count = 0
    for i in range(size):
        if data[size * (i + 1) - i - 1] == marker_player_1:
            marker_player_1_count += 1
        if data[size * (i + 1) - i - 1] == marker_player_2:
            marker_player_2_count += 1
        # print(f'проверка диагонали (ячейка) {size * (i + 1) - i - 1}- Player1: {marker_player_1_count}')
        if marker_player_1_count == count_for_win:
            return 1
        # print(f'проверка диагонали (ячейка) {size * (i + 1) - i - 1}- Player2: {marker_player_2_count}')
        if marker_player_2_count == count_for_win:
            return 2
    return 0


def get_count_free_place(data):
    count = 0
    for d in data:
        if d == '-':
            count += 1
    return count


def get_move_player(count_place):
    id_place_str = input('введите номер ячейки: ')
    if not id_place_str.isdigit() or int(id_place_str) < 1 or int(id_place_str) > count_place:
        print(f'значение должно быть (от {1} до {count_place})!')
        return 0
    return int(id_place_str)


def start_game(size, player1_settings, player2_settings):
    data = ['-'] * (size ** 2)
    print_table(size, data)

    id_move_player = 1
    id_player, name_player, marker_player = player1_settings

    id_player_win = get_player_id_win(size, data)
    while id_player_win == 0:
        if get_count_free_place(data) == 0:
            break

        print(f'Текущий ход игрока {name_player}')
        id_place_in_data = get_move_player(size ** 2)
        while id_place_in_data == 0 or data[id_place_in_data - 1] != '-':
            if id_place_in_data == 0:
                print(f'Неверный ход! Ошибка ввода номера ячейки!')
            if data[id_place_in_data - 1] != '-':
                print(f'Неверный ход! Ячейка {id_place_in_data} занята!')
            id_place_in_data = get_move_player(size ** 2)

        data[id_place_in_data - 1] = marker_player
        print_table(size, data)

        if id_move_player == 1:
            id_move_player = 2
            id_player, name_player, marker_player = player2_settings
        else:
            id_move_player = 1
            id_player, name_player, marker_player = player1_settings

        id_player_win = get_player_id_win(size, data)

    return id_player_win


def lesson5_hometask03():
    print(
        '* 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.')

    # size_str = input('введите размер поля (от 3): ')
    # if not size_str.isdigit() or int(size_str) < 3:
    #     print('введённая строка должна быть числом (>3)!')
    #     return
    # size = int(size_str)
    size = 3

    # вывод правил игры
    print_rules(size)

    input()
    # ввод имени и определение параметров игры
    # player1_settings = get_settings(1)
    player1_settings = (1, 'Игрок1', 'X')
    id_player1, name_player1, marker_player1 = player1_settings
    # marker_player2 = 'X'
    # if marker_player1 == 'X':
    #     marker_player2 = '0'
    # player2_settings = get_settings(2, marker_player2)
    player2_settings = (2, 'Игрок2', '0')
    id_player2, name_player2, marker_player2 = player2_settings

    id_player_win = start_game(size, player1_settings, player2_settings)
    if id_player_win == 0:
        print('Игра окончена! Ничья!')
    if id_player_win == id_player1:
        print(f'Игра окончена! Победил игрок {name_player1}')
    if id_player_win == id_player2:
        print(f'Игра окончена! Победил игрок {name_player2}')
