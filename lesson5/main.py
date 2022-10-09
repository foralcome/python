import lesson5_hometask_01
import lesson5_hometask_02
import lesson5_hometask_03
import lesson5_hometask_04

def load_menu():
    menu = {0: 'exit'}
    menu[1] = 'Задача 1'
    menu[2] = 'Задача 2'
    menu[3] = 'Задача 3'
    menu[4] = 'Задача 4'
    return menu


def print_menu(menu):
    print('--------------------------------')
    for key_menu, title_menu in menu.items():
        print(key_menu, '-', title_menu)


def get_select_menu(menu):
    print_menu(menu)
    select = int(input('выберите пункт меню: '))
    while select not in menu.keys():
        print('error - указан неверный пункт меню!')
        select = int(input('выберите пункт меню: '))
    return select


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu = load_menu()
    select = 1
    while select != 0:
        select = get_select_menu(menu)
        if select == 0:
            break
        elif select == 1:
            lesson5_hometask_01.lesson5_hometask01()
        elif select == 2:
            lesson5_hometask_02.lesson5_hometask02()
        elif select == 3:
            lesson5_hometask_03.lesson5_hometask03()
        elif select == 4:
            lesson5_hometask_04.lesson5_hometask04()
        else:
            print('внимание - реализация пункта меню {} не готова!')
