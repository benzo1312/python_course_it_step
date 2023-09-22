from collections.abc import Iterable, Iterator

lst = [1, 2, 3]
s = "text_text1_text2"
dic = {"a": 1, "b": 2, "c": 3}
num = 10

print(isinstance(lst, Iterator))
print(isinstance(lst, Iterable))


# print(type(lst))
# print(type(s))
# print(type(dic))

# print(dir(lst))
# print(dir(s))
# print(dir(dic))
# print(dir(num))

list_iter = iter(lst)
# print(type(list_iter))
# print(dir(list_iter))
# print(isinstance(list_iter, Iterator))
# print(isinstance(list_iter, Iterable))

# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
#
# for i in list_iter:
#     print(i)
#