"""
Написать iterator-класс, который будет возвращать квадрат числа
в диапазоне 0 до 20, и связанный с ним  iterable-класс,
который будет возвращать итератор
"""


class MyIterator:
    def __init__(self):
        self.num = 0

    def __next__(self):
        result = self.num ** 2
        if self.num > 10:
            raise StopIteration("No more")
        self.num += 1
        return result

class MyIterable:
    def __iter__(self):
        return MyIterator()

l = MyIterable()
print()
