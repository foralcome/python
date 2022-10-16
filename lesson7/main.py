import phone_dictionary
import user_interface as ui

if __name__ == '__main__':
    print('2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.')

    phone_dictionary.init()

    main_menu = ui.load_menu_main()
    select_main_menu = 1
    while select_main_menu != 0:
        ui.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        select_main_menu = ui.get_select_menu(main_menu)
        if select_main_menu == 0:
                break

        ui.run_command(select_main_menu)
