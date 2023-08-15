"""
Написать декоратор `@do_twice`, который будет вызывать любую функцию дважды.
"""


def go_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)

    return wrapper


@go_twice
def func_1(a):
    print(f'Hello my friend {a}')


func_1(input('What is your name? : '))
