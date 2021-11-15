"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

random.seed(42)
lst_1 = [random.randint(-100, 100) for _ in range(15)]
print(lst_1)


def func(lst: list):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i += 1
        n += 1
    return lst


def bubble_sort(arr):
    k = 0
    n = len(arr)
    gc = 0
    while True:
        c = 0
        for i in range(n - k - 1):
            j = n - i - 1
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                c += 1
                gc += 1
        if c == 0:
            break
    return arr


# второй метод нашел в интернете

print(bubble_sort(lst_1))
print(func(lst_1))
# [63, -72, -94, 89, -30, -38, -43, -65, 88, -74, 73, 89, 39, -78, 51] - наш список
# [89, 89, 88, 73, 63, 51, 39, -30, -38, -43, -65, -72, -74, -78, -94] - отсортированный
