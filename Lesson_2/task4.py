"""
 Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов: '))
i = 0
range_number = 1
total = 0
while i < n:
    total += range_number
    range_number /= -2
    i += 1

print(f'Сумма {total}')
