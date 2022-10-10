def get_dictionary_names(names):
    d = {}
    for name in names:
        if not name[0] in d:
            d[name[0]] = []
            d[name[0]].append(name)
        else:
            d[name[0]].append(name)

    return dict(sorted(d.items()))


def lesson6_hometask03():
    print(
        '3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.')

    names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
    print(names)
    print(get_dictionary_names(names))
