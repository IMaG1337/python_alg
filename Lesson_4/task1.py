"""
(Определить, какое число в массиве встречается чаще всего.) - задание

 Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
"""
from collections import Counter
from random import randint
import cProfile


def test1():
    lst = [randint(1, 10000000) for _ in range(5000)]
    a = Counter(lst)
    print(f'{list(a.keys())[list(a.values()).index(max(a.values()))]} '
          f'встречается в массиве {max(a.values())} раз(а)')


def test2():
    lst = [randint(1, 10000000) for _ in range(5000)]
    number = lst[0]
    max_numbers = 1
    for i in range(len(lst) - 1):
        frq = 1
        for k in range(i + 1, len(lst)):
            if lst[i] == lst[k]:
                frq += 1
        if frq > max_numbers:
            max_numbers = frq
            number = lst[i]
    print(f'{number} встречается в массиве {max_numbers} раз(а)')


def main():
    test1()
    test2()


cProfile.run('main()')

#  В среднем получилось где то в 58 раз первое решение быстрее чем 2е
#  Если range в списке увеличить до 50000 то 2-й метод выполняет 68 сек вместо 0,110 в 1-м методе
# Вывод данных : 1511967 встречается в массиве 2 раз(а)
#                737339 встречается в массиве 2 раз(а)
# 1    0.000    0.000    0.012    0.012 task1.py:9(test1) - первый вариант
# 1    0.685    0.685    0.696    0.696 task1.py:16(test2) - второй вариант
