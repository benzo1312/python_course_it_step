"""
Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел содержится одновременно
как в первом списке, так и во втором.
"""

lst = set(list(map(int, input().split())))
lst_ = set(list(map(int, input().split())))
print(len(lst & lst_))
