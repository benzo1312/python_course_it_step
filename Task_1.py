"""
Написать программу конвертер рублей в любые три валюты (обратное действие не требуется).
На вход программа принимает сумму в бел. рублях и валюту, в которую нужно ее перевести
(Например, EUR). Результат округлить до 2-х значимых цифр.Организовать функции в модули и пакет
"""

from currency import dev

money = int(input())
currency = input().lower()

print(dev.curr(money, currency))