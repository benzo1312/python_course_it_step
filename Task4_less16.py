"""
Написать рекурсивную функцию get_fib(n: int) -> int поиска значения n-го числа Фибоначчи
"""


def get_fib(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return get_fib(n - 1) + get_fib(n - 2)


print(get_fib(int(input())))
