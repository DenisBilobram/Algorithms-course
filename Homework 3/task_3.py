"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
count = 0
my_str = "papa"
uniq = []
for i in range(len(my_str)):
    for j in range(len(my_str), 0, -1):
        if my_str[i:j] not in uniq and my_str[i:j] != my_str:
            uniq.append(my_str[i:j])
            count += 1     