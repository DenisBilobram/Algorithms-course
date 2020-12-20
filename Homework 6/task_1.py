"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile

@profile
def my_func(x=int(input("Enter a positive number: ")), y=int(input("Enter a negtive degree: "))):
    if y == -1:
        result = 1 / x
        print(result)
    elif y < -1:
        i = 2
        degree = x
        while i <= abs(y):
            degree = degree * x
            i += 1
        result = 1 / degree
        print(result)
my_func()

# У меня по какой-то причине при любом скрипте использование памяти 13.1 MiB.
# Стоит windows 10 ltsc 64 bit. Python 3.8.5 32-bit

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     18     13.1 MiB     13.1 MiB   @profile
#     19                             def my_func(x=int(input("Enter a positive number: ")), y=int(input("Enter a negtive degree: "))):
#     20     13.1 MiB      0.0 MiB       if y == -1:
#     21                                     result = 1 / x
#     22                                     print(result)
#     23     13.1 MiB      0.0 MiB       elif y < -1:
#     24     13.1 MiB      0.0 MiB           i = 2
#     25     13.1 MiB      0.0 MiB           degree = x
#     26     13.1 MiB      0.0 MiB           while i <= abs(y):
#     27     13.1 MiB      0.0 MiB               degree = degree * x
#     28     13.1 MiB      0.0 MiB               i += 1
#     29     13.1 MiB      0.0 MiB           result = 1 / degree
#     30     13.2 MiB      0.0 MiB           print(result)