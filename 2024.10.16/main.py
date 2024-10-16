# Написать функцию для генерации строки из n строчных латинских букв

import random


def generate_lowercase_string(n):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(lowercase_letters) for _ in range(n))


if __name__ == '__main__':
    n = 5
    result = generate_lowercase_string(n)
    print(result)
