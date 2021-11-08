"""
(Определить, какое число в массиве встречается чаще всего.) - задание
 Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
"""
from collections import Counter
from random import randint
from memory_profiler import profile


def test1():
    lst = [randint(1, 100000000000000) for _ in range(5000)]
    a = Counter(lst)
    print(f'{list(a.keys())[list(a.values()).index(max(a.values()))]} '
          f'встречается в массиве {max(a.values())} раз(а)')


def test2():
    lst = [randint(1, 10000000000000) for _ in range(5000)]
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


@profile
def main():
    test1()
    test2()


main()
# 33863972171545 встречается в массиве 1 раз(а)
# 1312956751030 встречается в массиве 1 раз(а)
# Filename: C:\Python_Geek\PycharmProjects\pythonProject\python_algr\Lesson6\task1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     31     19.3 MiB     19.3 MiB           1   @profile
#     32                                         def main():
#     33     19.4 MiB      0.2 MiB           1       test1()
#     34     19.5 MiB      0.1 MiB           1       test2()
