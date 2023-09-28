"""
Реализуйте класс-итератор EvenRange, который принимает начало и конец интервала в качестве аргументов `__init__` и дает
только чётные числа во время итерации.
Если пользователь пытается итерироваться после того, как он дал все возможные числа, должно быть напечатано `Out of
numbers!` Примечание: Не используйте функцию `range()`
"""


class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start % 2 != 0:
            self.start +=1
            return self.start
        elif self.start % 2 == 0 and self.start < self.end - 1:
            self.start += 2
            res = self.start
            return res
        else:
            raise StopIteration('Out of numbers!')

    def __iter__(self):
        return


range_ = EvenRange(1,15)
print(next(range_))
print(next(range_))
print(next(range_))
print(next(range_))
print(next(range_))
print(next(range_))
print(next(range_))
print(next(range_))




