"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

lst = [i for i in range(2, 100)]
lst2 = [i for i in range(2, 10)]
lst3 = []

for i in lst:
    for a in lst2:
        if i % a == 0:
            lst3.append(i)

print(len(lst3))

print(lst3)
