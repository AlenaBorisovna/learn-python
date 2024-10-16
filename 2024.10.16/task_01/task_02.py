# Написать функцию для генерации строки из n строчных и заглавных латинских букв
# Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
# А если параметр use_uppercase не указан при использовании функции,
# то генерируем строку только из строчных букв.

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_string(n, use_uppercase=False):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letters = lowercase_letters
    if use_uppercase:
        letters += uppercase_letters

        return ''.join(random.choice(letters) for _ in range(n))


if __name__ == '__main__':
    n = 15
    result = generate_string(n, use_uppercase=True)
    print(result)
