"""
Напишите класс-итератор,
объекты которого генерируют случайные целые числа в количестве и в диапазоне,
которые передаются в конструктор
"""
import random


class RandomIterator:
    def __init__(self, n, start, end):
        self.n = n
        self.start = start
        self.end = end

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return random.randint(self.start, self.end)
        raise StopIteration('End')

    def __iter__(self):
        return self


rand_int = RandomIterator(5, 5, 10)
# print(next(rand_int))
# print(next(rand_int))
# print(next(rand_int))
# print(next(rand_int))
# print(next(rand_int))
# print(next(rand_int))

for num in rand_int:
    print(num)
