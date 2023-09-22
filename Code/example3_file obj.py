from collections.abc import Iterable, Iterator

f = open('test.txt')

print(dir(f))
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))

# print(next(f))
# print(next(f))
# print(next(f))


print(f.__next__())
print(f.__next__())
print(f.__next__())

f.close()
