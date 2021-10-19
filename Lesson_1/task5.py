# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string

a = input('Введите первую букву ').lower()
b = input('Введите вторую букву ').lower()

lst = list(string.ascii_letters)[0:26]
print(f'Буква {a} находится на {len(lst[:lst.index(a)+1])} месте\n'
      f'Буква {b} находится {len(lst[:lst.index(b)+1])} месте\n'
      f'Между ними {len(lst[lst.index(a):lst.index(b)])-1} букв')
