import random


def get_random_joke(count, nouns, adverbs, adjectives):
    jokes = []
    for i in range(count):
        jokes.append(random.choice(nouns * 2) + ' ' + random.choice(adverbs * 2) + ' ' + random.choice(adjectives * 2))
    return jokes


def lesson6_hometask05():
    print(
        '** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого).')

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    count_str = input('введите количество элементов списка: ')
    if not count_str.isdigit() or int(count_str) < 1:
        print('введённая строка должна быть числом (>0)!')
        return
    count = int(count_str)

    print(get_random_joke(count, nouns, adverbs, adjectives))
