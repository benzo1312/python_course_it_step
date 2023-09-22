"""
Напишите генераторную функцию для задания 2.
В качестве аргументов она должна принимать количество элементов и диапазон.
"""
import random


def nums_generator(n, start, end):
    while n > 0:
        yield random.randint(start, end)
        n -= 1

g = nums_generator(5, 10, 20)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
