"""
 Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.
"""

M = 5
number = 4
lst = []
for i in range(number):
    b = []
    s = 0
    print(f'{i}я строка: ')
    for j in range(M-1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    lst.append(b)
for i in lst:
    print(*i)
