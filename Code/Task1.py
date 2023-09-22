"""
Написать iterator-класс, который будет возвращать квадрат числа
в диапазоне 0 до 20, и связанный с ним  iterable-класс,
который будет возвращать итератор
"""


class SquareIterator:
    def __init__(self):
        self.count = 0

    def __next__(self):
        res = self.count ** 2
        if self.count > 5:
            raise StopIteration
        self.count += 1
        return res


class SquareIterable:
    def __iter__(self):
        return SquareIterator()


sqr_iter = iter(SquareIterable())

print(next(sqr_iter))
print(next(sqr_iter))
print(next(sqr_iter))
print(next(sqr_iter))
print(next(sqr_iter))
print(next(sqr_iter))
print(next(sqr_iter))
