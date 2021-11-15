"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import randint, seed

seed(42)
lst = [randint(0, 50) for _ in range(10)]


def merge_two(left, right):
    c = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i < len(left):
        c += left[i:]
    if j < len(right):
        c += right[j:]
    return c


def merge_sort(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list
    middle = len(numbers_list) // 2
    left = merge_sort(numbers_list[:middle])
    right = merge_sort(numbers_list[middle:])
    return merge_two(left, right)


print(merge_sort(lst))
