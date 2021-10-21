"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def numbers():
    one_number = input('Введите первое число: ')
    two_number = input('Введите второе число: ')
    three_number = input('Введите третье число: ')
    x = [[int(a) for a in one_number],
         [int(a) for a in two_number],
         [int(a) for a in three_number]]
    maximum = max((sum(x[0]), sum(x[1]), sum(x[2])))
    if maximum == sum(x[0]):               # можно как то не делать проверку через if а найти более лаконичным образом?
        return f'Наибольшее число по сумме цифр {one_number}, сумма цифр = {maximum}'
    elif maximum == sum(x[1]):
        return f'Наибольшее число по сумме цифр {two_number}, сумма цифр = {maximum}'
    elif maximum == sum(x[2]):
        return f'Наибольшее число по сумме цифр {three_number}, сумма цифр = {maximum}'


print(numbers())
