"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
lst = [235, 52353, 6343, 12, 43, 5646, 1, 666, 444]
maximum = lst.index(max(lst))  # узнаем идекс максимального числа в списке
minimum = lst.index(min(lst))  # узнаем индекс минимального числа в списке
lst[maximum], lst[minimum] = lst[minimum], lst[maximum]  # меняем их местами
print(lst)
