"""Написать функцию для генерации строки из n строчных и заглавных латинских букв, а также числе и символов
Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв.
По тому же сценарию добавляем контроль использования цифр и символов"""

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_random_string(n, use_uppercase=False, use_digits=False, use_punctuation=False) -> str:
    letters: str = ascii_lowercase

    if use_uppercase:
        letters += ascii_uppercase

    if use_digits:
        letters += digits

    if use_punctuation:
        letters += punctuation

    return ''.join(random.choice(letters) for _ in range(n))


if __name__ == '__main__':
    n = 15
    print(generate_random_string(n, use_uppercase=True))
    print(generate_random_string(n, use_uppercase=True, use_digits=True))
    print(generate_random_string(n, use_uppercase=True, use_digits=True, use_punctuation=True))
