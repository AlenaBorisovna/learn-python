# Написать функцию для генерации строки из n строчных и заглавных латинских букв
# Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
# А если параметр use_uppercase не указан при использовании функции,
# то генерируем строку только из строчных букв.

import random
from string import ascii_lowercase, ascii_uppercase


def generate_random_string(n, use_uppercase=False) -> str:
    letters: str = ascii_lowercase

    if use_uppercase:
        letters += ascii_uppercase

        return ''.join(random.choice(letters) for _ in range(n))


if __name__ == '__main__':
    n = 15
    result = generate_random_string(n, use_uppercase=True)
    print(result)
