# Напишите программу, которая
# 1. генерирует 10 000 строк из цифр, строчных и заглавных букв длинной 100 символов,
# 2. записывает их в файл text.txt
# 3. архивирует его в text.zip

import random
import string
import zipfile


def gen_string(length):
    ch = string.ascii_letters + string.digits
    return ''.join(random.choice(ch) for _ in range(length))


with open('text.txt', 'w') as file:
    for _ in range(10000):
        file.write(gen_string(100) + '\n')

with zipfile.ZipFile('text.txt', 'w', encodings='UTF-8') as zip_file:
    zip_file.write('text.txt')
