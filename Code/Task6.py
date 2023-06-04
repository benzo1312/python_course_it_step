"""
ROT13 — это простой шифр, который заменяет каждую букву строки буквой,
которая находится на 13 букв после неё в алфавите. Программа получает на вход строку,
необходимо зашифровать её с помощью ROT13 и вывести результат.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = 13
text = input()
result = ''

for item in text:
    if item == ' ':
        result += ' '
    else:
        new_index = (alphabet.find(item) + n) % len(alphabet)
        result += alphabet[new_index]
print('Result: "' + result + '"', end='')