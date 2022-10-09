import random
import re


def print_rules(game_settings):
    count_all_candy, max_count_candy_player, mode_game = game_settings
    print(
        f'Условие задачи: На столе лежит {count_all_candy} конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n\
За один ход можно забрать не более чем {max_count_candy_player} конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять\n\
первому игроку, чтобы забрать все конфеты у своего конкурента?')
    print('...для продолжения нажмите на любую клавишу...')
    input()


def set_game_settings():
    count_all_candy_str = input('Введите количество конфет: ')
    if not count_all_candy_str.isdigit() or int(count_all_candy_str) < 0:
        print('введённая строка должна быть числом (>0)! установлено значение по умолчанию: 101')
        count_all_candy = 101
    else:
        count_all_candy = int(count_all_candy_str)

    max_count_candy_player_str = input('Введите max количество конфет за ход: ')
    if not max_count_candy_player_str.isdigit() or int(max_count_candy_player_str) < 0:
        print('введённая строка должна быть числом (>0)! установлено значение по умолчанию: 17')
        max_count_candy_player = 17
    else:
        max_count_candy_player = int(max_count_candy_player_str)

    mode_game_str = input('Введите режим игры (1 - игра с ботом, 2 игра с игроком): ')
    if not mode_game_str.isdigit() or (int(mode_game_str) != 1 and int(mode_game_str) != 2):
        print('введён неверный режим игры! установлен режим по умолчанию: 1 - игра с ботом')
        mode_game = 1
    else:
        mode_game = int(mode_game_str)

    return (count_all_candy, max_count_candy_player, mode_game)


def get_input_candy_player(current_count_candy, max_count_candy_player, type_player='bot'):
    if type_player == 'bot':
        count_candy_player = current_count_candy % max_count_candy_player - 1
        if count_candy_player == 0:
            count_candy_player = max_count_candy_player
        print(f'Количество конфет ({type_player}): {count_candy_player}')
    else:
        count_candy_player_str = input('Введите количество конфет: ')
        if not count_candy_player_str.isdigit() or int(count_candy_player_str) < 1 or int(
                count_candy_player_str) > max_count_candy_player:
            print(f'значение должно быть (от {1} до {max_count_candy_player})!')
            return 0
        count_candy_player = int(count_candy_player_str)

    return count_candy_player


def print_current_count_candy(count_all_candy, max_count_candy_player, current_count_candy):
    print(f'Текущее количество конфет: {current_count_candy}')


def start_game(game_settings, player1_settings, player2_settings, id_player_first=1):
    count_all_candy, max_count_candy_player, mode_game = game_settings
    current_count_candy = count_all_candy

    id_move_player = id_player_first
    if id_move_player == 1:
        id_player, name_player, type_player = player1_settings
    else:
        id_player, name_player, type_player = player2_settings

    while True:
        if current_count_candy <= max_count_candy_player:
            break

        print(f'\nТекущий ход игрока {name_player}')

        count_candy_player = get_input_candy_player(current_count_candy, max_count_candy_player, type_player)
        current_count_candy -= count_candy_player

        print_current_count_candy(count_all_candy, max_count_candy_player, current_count_candy)

        if id_move_player == 1:
            id_move_player = 2
            id_player, name_player, type_player = player2_settings
        else:
            id_move_player = 1
            id_player, name_player, type_player = player1_settings

    return id_move_player


def lesson5_hometask04():
    print('** 4. Создайте программу для игры с конфетами человек против человека.')

    # ввод имени и определение параметров игры
    game_settings = set_game_settings()
    count_all_candy, max_count_candy_player, mode_game = game_settings

    # вывод правил игры
    print_rules(game_settings)

    print('--------------------------------------------')
    print(f'Всего конфет: {count_all_candy}')
    print(f'За ход можно взять не более: {max_count_candy_player}')

    if mode_game == 1:
        print('Режим игры: Игра против бота')
        player1_settings = (1, 'Игрок1', 'player')
        player2_settings = (2, 'Игрок2', 'bot')
    else:
        print('Режим игры: Игра против игрока')
        player1_settings = (1, 'Игрок1', 'player')
        player2_settings = (2, 'Игрок2', 'player')

    id_player1, name_player1, type_player1 = player1_settings
    id_player2, name_player2, type_player2 = player2_settings

    id_player_first = 1
    if random.randint(1, 1000) % 2 == 0:
        id_player_first = 2
    print(f'Игру начинает игрок {id_player_first}')

    print('\n------ START GAME ----------------------------')

    id_player_win = start_game(game_settings, player1_settings, player2_settings, id_player_first)

    print('\n------ STOP GAME -----------------------------')
    if id_player_win == id_player1:
        print(f'Игра окончена!\nПобедил игрок {name_player1}({type_player1})\n')
    if id_player_win == id_player2:
        print(f'Игра окончена!\nПобедил игрок {name_player2}({type_player2})\n')
