"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def check(n):
    addition = [i for i in range(1, n+1)]
    multiplication = n*(n+1)/2
    return f'1+2+...+{n} = {sum(addition)}\n' \
           f'{n}({n}+1)/2 = {int(multiplication)}'


print(check(25))
