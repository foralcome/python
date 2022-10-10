def get_dictionary_soname_name(names):
    d_soname = {}
    for sn in names:
        name, soname = sn.split()
        if not soname[0] in d_soname:
            d_soname[soname[0]] = {}
        if not name[0] in d_soname[soname[0]]:
            d_soname[soname[0]][name[0]] = []
        d_soname[soname[0]][name[0]].append(sn)
        d_soname[soname[0]] = dict(sorted(d_soname[soname[0]].items()))
    return dict(sorted(d_soname.items()))


def lesson6_hometask04():
    print(
        '3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.')

    print('Исходный список сотрудников:')
    names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
             "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
    print(names)

    print()
    print('Итоговый словарь сотрудников:')
    print(get_dictionary_soname_name(names))
