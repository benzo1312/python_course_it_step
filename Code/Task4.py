"""
Создай список, состоящий из N элементов, которые указываются функцией ввода данных.
Первым вводом укажи размер списка (N), далее — элементы списка.
Требуется найти наименьший нечётный элемент данного списка, если такого элемента нет — вывести 0.
"""

n = int(input())
res = []
i = 0

while i < n:
    if i % 2 != 0:
        res.append(i)
    i += 1
res.sort()
print(res[0])
# вариант без сорт
# print(min(res))
