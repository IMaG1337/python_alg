# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

number_letter = int(input('Введите номер буквы в алфавите\n'))
lst = list(string.ascii_letters)[0:26]
if number_letter <= 26:
    print(f'Ваша буква {lst[number_letter-1]}')
else:
    print('Букв в алфавите 26, попробуйте ещё :)')

