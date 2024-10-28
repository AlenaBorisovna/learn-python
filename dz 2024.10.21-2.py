# Напишите программу, которая
# 1. разархивирует text.zip
# 2. читает файл text.txt
# 3. выводит все строки на экран
# 4. выводит 5 самых повторяющихся символов на экран и количество их повторений
import io
import zipfile
from pathlib import Path
from collections import Counter

PATH_FILE: str = 'C:\\Users\\user.A1PC08\Documents\Кудряшова\learn-python\\text.zip'

# 1. разархивирует text.zip
with zipfile.ZipFile(PATH_FILE, "r") as zip_ref:
    with zip_ref.open("text.txt") as text_file:
        content = io.TextIOWrapper(text_file).read()

# 2. читает файл text.txt
# 3. выводит все строки на экран
print("Весь текст файла: ")
print(content)

# 4. выводит 5 самых повторяющихся символов на экран и количество их повторений
char_count = Counter(content.lower())
sorted_chars = char_count.most_common(5)

print("5 повторяющих символов: ")
for char, count in sorted_chars:
    print(f"{char}: {count}")
