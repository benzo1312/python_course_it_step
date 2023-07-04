"""
Создать функцию-замыкание create_dict, она должна сохранять в себе все значения,
которые ей будут переданы причем в виде словаря.
Ключами данного словаря должны быть натуральные числа, равные номеру вызова данной функции.

f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict() # создаем новое замыкание в f_2
print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.

При каждом вызове должен возвращаться словарь, хранящийся в замыкании
"""


def create_dict():
    d = dict()
    count = 1

    def insert_value(val):
        nonlocal count
        d[count] = val
        count += 1
        return d

    return insert_value


f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

print(globals()['f_1'])
