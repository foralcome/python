import glob, os
import lesson4_hometask_04

def get_list_files_equations():
    files = []
    for file in glob.glob("*.txt"):
        files.append(file)
    return files


def print_list_files_equations(files):
    i = 1
    for file in files:
        print(f'{i}) {file}')
        i += 1

def get_count_rows_in_file_equation(file_name):
    count_rows = 0
    with open(file_name, 'r') as file_equation:
        for line in file_equation:
            count_rows += 1
    return count_rows

def load_equation_strings_from_file(file_name):
    rows = []
    with open(file_name, 'r') as file_equation:
        for line in file_equation:
            line = line.rstrip()
            if len(line) != 0:
                rows.append(line)
    return rows

def get_union_equations_data(equations_data_1, equations_data_2):
    max_degree_equation_1 = len(equations_data_1)
    max_degree_equation_2 = len(equations_data_2)
    max_degree = max(max_degree_equation_1, max_degree_equation_2)
    union_data = []
    for i in range(max_degree):
        if i < max_degree_equation_1 and i < max_degree_equation_2:
            union_data.append(equations_data_1[i] + equations_data_2[i])
        elif i < max_degree_equation_1:
            union_data.append(equations_data_1[i])
        else:
            union_data.append(equations_data_2[i])
    return union_data

def lesson4_hometask05():
    print('** 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов')

    files = get_list_files_equations()
    if len(files) == 0:
        print('файлы не найдены!')
    elif len(files) < 2:
        print('количество файлов должно быть больше 1')
    else:
        print('список найденый файлов:')
        print_list_files_equations(files)

        file_1_str = input('введите номер первого файла: ')
        if not file_1_str.isdigit():
            print('введённая строка должна быть числом (>0)!')
            return
        file_1 = int(file_1_str)
        if file_1 > len(files):
            print('номер файла не определён!')
            return

        file_2_str = input('введите номер второго файла: ')
        if not file_2_str.isdigit():
            print('введённая строка должна быть числом (>0)!')
            return
        file_2 = int(file_2_str)
        if file_1 > len(files):
            print('номер файла не определён!')
            return

        if file_1 == file_2:
            print('файлы должн быть разными!')
        else:
            name_file_1 = files[file_1-1];
            print(f'загружаем многочлены из файла {name_file_1}!')
            equation_strings_file_1 = load_equation_strings_from_file(name_file_1)
            count_rows_file_1 = len(equation_strings_file_1)
            print(f'в файле {name_file_1} обнаружено {count_rows_file_1} строк')

            name_file_2 = files[file_2 - 1];
            print(f'загружаем многочлены из файла {name_file_2}!')
            equation_strings_file_2 = load_equation_strings_from_file(name_file_2)
            count_rows_file_2 = len(equation_strings_file_2)
            print(f'в файле {name_file_2} обнаружено {count_rows_file_2} строк')

            if count_rows_file_1 != count_rows_file_2:
                print('количество многочленов в файлах должно совпадать!')
            else:
                for i in range(count_rows_file_1):
                    print('объединение многочлена файлов')
                    print('1)',equation_strings_file_1[i])
                    parse_equation_1_data = lesson4_hometask_04.parse_equation_multi_degree_string(
                        equation_strings_file_1[i])
                    #parse_equation_1_str = lesson4_hometask_04.get_equation_multi_degree_string(parse_equation_1_data)
                    #print(parse_equation_1_str)

                    print('2)',equation_strings_file_2[i])
                    parse_equation_2_data = lesson4_hometask_04.parse_equation_multi_degree_string(
                        equation_strings_file_2[i])
                    #parse_equation_2_str = lesson4_hometask_04.get_equation_multi_degree_string(parse_equation_2_data)
                    #print(parse_equation_2_str)

                    union_equations_data = get_union_equations_data(parse_equation_1_data, parse_equation_2_data)
                    union_equation_str = lesson4_hometask_04.get_equation_multi_degree_string(union_equations_data)
                    print('+)',union_equation_str)
                    union_file_name = os.path.splitext(name_file_1)[0] + '_' + os.path.splitext(name_file_2)[0] + '.uni'
                    lesson4_hometask_04.write_equation_to_file(union_equation_str, file_name=union_file_name)
