from collections.abc import Iterable, Iterator


class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        raise StopIteration('End of iter')


class MyIterable:
    def __iter__(self):
        return MyIterator(3)


my_iter = iter(MyIterable())
print(dir(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# for i in my_iter:
#     print(i)

print(isinstance(my_iter, Iterator))
print(isinstance(my_iter, Iterable))
print(len(my_iter))
