"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint, seed
from statistics import median
seed(42)
lst = [randint(0, 100) for _ in range(0, (2*int(input('Введите натуральное число: '))+1))]
print(f'Наш массив - {lst}')
print(f'Медиана нашего массива -  {median(lst)}')
