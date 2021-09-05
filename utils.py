from random import randint, shuffle, choice
from collections import Counter


class WrongTaskInput(Exception):
    pass


def get_random(input_list):
    i = randint(0, len(input_list) - 1)
    return input_list[i], input_list[:i] + input_list[i + 1:]


def get_input(max_size=256):

    list_size = randint(1, max_size)

    if randint(1, 10) == 1:
        # generate list with uniques elements
        input_list = list(range(list_size))
        shuffle(input_list)
    else:
        # generate list with random element frequency
        alphabet = range(randint(1, list_size))
        input_list = [choice(alphabet) for _ in range(list_size)]

    k = randint(0, list_size)

    return input_list, k


def is_subset(list_1, list_2):
    counter_1 = Counter(list_1)
    counter_2 = Counter(list_2)
    for k, v in counter_1.items():
        if counter_2[k] < v:
            return False
    return True
