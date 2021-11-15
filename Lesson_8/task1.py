"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

my_string = input('Введите вашу строку, только маленькими латинскими буквами: ').lower()
set_string = set()
for num in range(len(my_string)):
    for number in range(len(my_string), num, -1):
        set_string.add(hashlib.sha1(my_string[num:number].encode('utf-8')).hexdigest())

print(f'Колличество вхождений: {len(set_string)}')
