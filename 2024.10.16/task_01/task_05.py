"""Переделайте функцию в класс RandomGenerator, в конструктор он принимает то же, что и функция в 4-й задаче.
Объект генерирует строку в методе get_string().
Также у него должен быть метод генерирующий строку только строчных букв, только заглавных букв, только цифр и только символов.
"""

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class RandomGenerator:

    def __init__(self, n, use_uppercase=False, use_digits=False, use_punctuation=False):
        self.n: int = n
        self.use_uppercase: bool = use_uppercase
        self.use_digits: bool = use_digits
        self.use_punctuation: bool = use_punctuation

    def get_string(self) -> str:
        letters: str = ascii_lowercase

        if self.use_uppercase:
            letters += ascii_uppercase

        if self.use_digits:
            letters += digits

        if self.use_punctuation:
            letters += punctuation

        return ''.join(random.choice(letters) for _ in range(self.n))


if __name__ == '__main__':
    random_gen = RandomGenerator(10)
    print(random_gen.get_string())
    random_gen = RandomGenerator(10, use_uppercase=True)
    print(random_gen.get_string())
    random_gen = RandomGenerator(10, use_uppercase=True, use_digits=True)
    print(random_gen.get_string())
    random_gen = RandomGenerator(10, use_uppercase=True, use_digits=True, use_punctuation=True)
    print(random_gen.get_string())
