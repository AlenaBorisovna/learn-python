"""Добавьте в генератор опцию, которая будет контролировать
разрешены ли в строке повторяющиеся символы.
И если не разрешены, то нельзя допускать повторяющихся символов в строке."""

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_random_string(n, use_uppercase=False, use_digits=False, use_punctuation=False, allow_duplicates=True) -> str:
    letters: str = ascii_lowercase

    if use_uppercase:
        letters += ascii_uppercase

    if use_digits:
        letters += digits

    if use_punctuation:
        letters += punctuation

    result = list()

    if not allow_duplicates:
        letters_unique = set()
        while len(letters_unique) < n:
            let = random.choice(letters)
            letters_unique.add(let)
        result = list(letters_unique)

    else:
        result = [random.choice(letters) for _ in range(n)]

    return ''.join(result)


if __name__ == '__main__':
    n = 15
    print(generate_random_string(n, use_uppercase=True))
    print(generate_random_string(n, use_uppercase=True, use_digits=True))
    print(generate_random_string(n, use_uppercase=True, use_digits=True, use_punctuation=True))
