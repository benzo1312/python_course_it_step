"""
Реализуйте генератор, который будет бесконечно генерировать нечётные числа.
"""

def infinity_gen(num):
    if num // 2  == 0:
        while True:
            yield num
    if num // 2 != 0:
        num +=1
        while True:
            yield num
            num +=2


generator = infinity_gen(8)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

