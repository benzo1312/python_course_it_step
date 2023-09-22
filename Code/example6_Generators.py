from collections.abc import Iterable, Iterator


# def my_gen(num: int):
#     while num > 0:
#         yield num
#         num -= 1


# print(dir(my_gen(3)))
# print(isinstance(my_gen(3), Iterator))

# gen = my_gen(3)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# print(len(gen))


### RANGE - LAZY GENERATOR ###
"""
range - не является итератором, т.к. не реализует метод __next__()
"""

nums = range(0, 100)
square = (n**2 for n in nums)

# print(dir(nums))
# print(dir(square))
print(nums[-1])
print(square[-1])

# nums_iter = iter(nums)
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))


print(len(nums))
# print(len(nums_iter))
# print(len(square))
