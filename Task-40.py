import os

print("Файл существует") if os.path.isfile('./test.txt') else print("Файл не найден")