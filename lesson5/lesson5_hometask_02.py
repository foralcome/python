import glob, os
import re


def encode_string_rle(s):
    if len(s) == 0:
        return ''

    res = ''
    char_current = s[0]
    count_repeate = 1
    for i in range(len(s) - 1):
        if s[i + 1] == char_current:
            count_repeate += 1
        else:
            res += str(count_repeate) + char_current
            count_repeate = 1
            char_current = s[i + 1]
    res += str(count_repeate) + char_current
    return res


def decode_string_rle(s_rle):
    if len(s_rle) == 0:
        return ''

    res = ''
    index_num_start = 0
    for i in range(1, len(s_rle)):
        if s_rle[i].isalpha():
            index_num_stop = i - 1
            count_repeate = int(s_rle[index_num_start:index_num_stop + 1])
            res += s_rle[i] * count_repeate
            index_num_start = i + 1
    return res


def encode_file_rle(file_name_data, file_name_save):
    with open(file_name_data, 'r') as file_data, open(file_name_save, 'w') as file_data_rle:
        for line_data in file_data:
            file_data_rle.write(encode_string_rle(line_data.rstrip()) + '\n')


def decode_and_print_file_rle(file_name_rle):
    with open(file_name_rle, 'r') as file_data_rle:
        for line_data_rle in file_data_rle:
            print(decode_string_rle(line_data_rle.rstrip()))


def print_file(file_name):
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            print(line_data.rstrip())


def lesson5_hometask02():
    print(
        '2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.')

    # file_name_in_text = 'data.txt'
    file_name_in_text = input('Введите имя файла для кодирования: ')
    if not os.path.exists(file_name_in_text):
        print(f'File {file_name_in_text} not found')
        return
    print(f'Содержимое файла: {file_name_in_text}')
    print_file(file_name_in_text)

    file_name_out_text = input('Введите имя файла для сохранения: ')
    # file_name_out_text = 'data_rle.txt'

    print('')
    print(f'Кодирование файла {file_name_in_text} в {file_name_out_text} RLE алгоритмом')
    encode_file_rle(file_name_in_text, file_name_out_text)
    print(f'Содержимое файла: {file_name_out_text}')
    print_file(file_name_out_text)

    print('')
    print(f'Декодирование файла {file_name_out_text} файла RLE алгоритмом')
    decode_and_print_file_rle(file_name_out_text)
