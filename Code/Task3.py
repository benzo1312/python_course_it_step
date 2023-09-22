"""
Напишите генераторную функцию для задания 2.
В качестве аргументов она должна принимать количество элементов и диапазон.
"""
import random


def generate_random(num: int, start: int, end: int):
    while num > 0:
        yield random.randint(start, end)
        num -= 1


gen = generate_random(5, 5, 10)
print(next(gen))



