"""
Определить, какое число в массиве встречается чаще всего.
"""
from collections import Counter
lst = [1, 1, 1, 3, 54, 5643, 523, 542152, 2, 3, 2, 3, 1]
a = Counter(lst)

number = lst[0]
max_numbers = 1
for i in range(len(lst)-1):
    frq = 1
    for k in range(i+1, len(lst)):
        if lst[i] == lst[k]:
            frq += 1
    if frq > max_numbers:
        max_numbers = frq
        number = lst[i]


print(f'{number} встречается в массиве {max_numbers} раз(а)')
print(f'{list(a.keys())[list(a.values()).index(max(a.values()))]} '
      f'встречается в массиве {max(a.values())} раз(а)')
#  два варианта решения
