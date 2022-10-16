import phone_dictionary
import phone_dictionary_note
import file_phone_dictionary


def load_menu_main():
    menu = {}
    menu[1] = 'Вывести справочник на экран'
    menu[2] = 'Добавить новую запись в справочник'
    menu[3] = 'Удалить запись из справочника'
    menu[4] = 'Найти запись в справочника'
    menu[5] = 'Загрузить телефонный справочник из файла'
    menu[6] = 'Сохранить телефонный справочник в файла'
    menu[0] = 'выход'
    return menu


def load_menu_file_format():
    menu_format = {}
    menu_format[1] = 'CSV'
    menu_format[2] = 'JSON'
    menu_format[3] = 'XML'
    menu_format[0] = 'отмена'
    return menu_format


def print_menu(menu_title, menu_data):
    print(f'\n----- {menu_title} -----')

    for key_menu, title_menu in menu_data.items():
        print(key_menu, '-', title_menu)


def get_select_menu(menu):
    select = int(input('выберите пункт меню: '))
    while select not in menu.keys():
        print('error - указан неверный пункт меню!')
        select = int(input('выберите пункт меню: '))
    return select


def print_phone_dictionary_note(note):
    print(f"{note['soname']} {note['name']}, тел.{note['phone']} // {note['description']}")


def print_phone_dictionary(pd):
    if len(pd) == 0:
        print('В словаре нет записей')
    else:
        print('\nТелефонный справочник:')
        cur_letter = ''
        for letter in pd:
            if cur_letter == '' or cur_letter != letter:
                print(f'> {letter} <')
                cur_letter = letter
            for note in pd[letter]:
                print_phone_dictionary_note(note)


def add_phone_to_dictionary():
    soname = input('введите Фамилию: ')
    name = input('введите Имя: ')
    phone = input('введите Телефон: ')
    description = input('введите Примечание: ')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    note = phone_dictionary_note.create(soname, name, phone, description)
    return phone_dictionary.add_note(note)


def find_phone_from_dictionary():
    phone = input('введите Телефон: ')
    note = phone_dictionary.find_note_by_phone(phone)
    if note == None:
        print(f'Телефон {phone} не найден в телефонной книге!')
    else:
        print(f'Найден телефон {phone}')
        print_phone_dictionary_note(note)


def remove_phone_from_dictionary():
    phone = input('введите Телефон: ')
    if phone_dictionary.find_note_by_phone(phone) == None:
        print(f'Телефон {phone} не найден в телефонной книге!')
    return phone_dictionary.remove_note_by_phone(phone)


def run_command(menu_command=1):
    pd = phone_dictionary.get_phone_dictionary()
    if menu_command == 1:
        print_phone_dictionary(pd)
    if menu_command == 2:
        add_phone_to_dictionary()
        print_phone_dictionary(pd)
    if menu_command == 3:
        remove_phone_from_dictionary()
        print_phone_dictionary(pd)
    if menu_command == 4:
        find_phone_from_dictionary()
        print_phone_dictionary(pd)
    if menu_command == 5:
        menu_file_format = load_menu_file_format()
        print_menu('Формат файла', menu_file_format)
        select_menu_file_format = get_select_menu(menu_file_format)
        if select_menu_file_format == 1:
            file_phone_dictionary.load_phone_dictionary_from_file_csv()
        elif select_menu_file_format == 2:
            file_phone_dictionary.load_phone_dictionary_from_file_json()
        elif select_menu_file_format == 3:
            file_phone_dictionary.load_phone_dictionary_from_file_xml()
        else:
            return None
    if menu_command == 6:
        menu_file_format = load_menu_file_format()
        print_menu('Формат файла', menu_file_format)
        select_menu_file_format = get_select_menu(menu_file_format)
        if select_menu_file_format == 1:
            file_phone_dictionary.save_phone_dictionary_to_file_csv(pd)
        elif select_menu_file_format == 2:
            file_phone_dictionary.save_phone_dictionary_to_file_json(pd)
        elif select_menu_file_format == 3:
            file_phone_dictionary.save_phone_dictionary_to_file_xml(pd)
        else:
            return None

    else:
        return None
