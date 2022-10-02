import random
import re


def get_equation_multi_degree_data(max_degree):
    equation_values = []
    for degree in range(max_degree + 1):
        coef = random.randint(-5, 5)
        equation_values.append(coef)
    return equation_values


def write_equation_to_file(equation_str, file_name=''):
    if len(file_name) == 0:
        file_name = 'equation_file.txt'
    with open(file_name, "a", encoding="utf-8") as equation_file:
        equation_file.write(equation_str + '\n')


def get_equation_multi_degree_string(equation_values, is_zero_values=False):
    equation_str = ''
    for degree in range(len(equation_values) - 1, -1, -1):
        if is_zero_values and equation_values[degree] == 0:
            continue
        plus_minus = '+';
        if equation_values[degree] < 0:
            plus_minus = '-';
        if degree != 0:
            equation_str += f" {plus_minus} {abs(equation_values[degree])}*x^{degree}"
        else:
            equation_str += f" {plus_minus} {abs(equation_values[degree])}"
    return equation_str + ' = 0'


def parse_equation_multi_degree_string(equation_string):
    max_degree = 0
    equation_dict = {}
    for result_reg in re.findall(r'[\+\-\s]+[0-9]+\*x\^[0-9]+', equation_string):
        result_reg = result_reg.replace(' ', '')
        value, degree = int(result_reg.split('*x^')[0]), int(result_reg.split('*x^')[1])
        if max_degree < degree:
            max_degree = degree
        equation_dict[degree] = value

    match_degree_0 = re.search(r'[\+\-\s]+[0-9]+\s\=\s0', equation_string)
    if match_degree_0 != None:
        value_degree_0 = equation_string[match_degree_0.start():match_degree_0.end()]
        value_degree_0 = value_degree_0.replace(' ', '')
        value_0, degree_0 = int(value_degree_0.split('=')[0]), int(value_degree_0.split('=')[1])
        equation_dict[degree_0] = value_0

    equation_values = []
    for i in range(max_degree + 1):
        if i in equation_dict.keys():
            equation_values.append(equation_dict[i])
        else:
            equation_values.append(0)

    return equation_values


def lesson4_hometask04():
    print('* 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов \
    (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз..')

    count_equations_str = input('введите количество многочленов: ')
    if not count_equations_str.isdigit():
        print('введённая строка должна быть числом (>0)!')
        return
    count_equations = int(count_equations_str)
    file_name = f'equation_file_{count_equations}.txt'

    for count in range(count_equations):
        print(f'многочлен {count + 1}:')
        degree_str = input(f'введите max степень: ')
        if not degree_str.isdigit() or int(degree_str) <= 0:
            print('введённая строка должна быть числом (>0)!')
            return
        degree = int(degree_str)
        print(f'многочлен {count + 1}: max степень {degree}')

        equation = get_equation_multi_degree_data(degree)
        equation_str = get_equation_multi_degree_string(equation)
        print(f'многочлен {count + 1}:', equation_str)

        write_equation_to_file(equation_str, file_name=file_name)
        print(f'многочлен {count + 1} записан в файл {file_name}')
