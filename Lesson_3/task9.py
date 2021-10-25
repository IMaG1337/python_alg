"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import random
M = 10
number = 5
a = []
for i in range(number):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print(f'{n}', end=' ')
    a.append(b)
    print()
mx = -1
for j in range(M):
    mn = 200
    for i in range(number):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print(f'Максимальный среди минимальных: {mx}')
