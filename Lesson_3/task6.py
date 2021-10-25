"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

lst = [randint(1, 100) for i in range(10)]
minimum = min(lst)
maximum = max(lst)
if lst.index(minimum) > lst.index(maximum):
    print(f'Сумма между самым минимальным значением и максимальным\n'
          f'нашего списка -> {lst}\n'
          f'Равна = {sum(lst[lst.index(maximum) + 1 :lst.index(minimum)])}')
else:
    print(f'Сумма между самым минимальным значением и максимальным\n'
          f'нашего списка -> {lst}\n'
          f'Равна = {sum(lst[lst.index(minimum) + 1 :lst.index(maximum)])}')
