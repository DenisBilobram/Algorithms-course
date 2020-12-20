"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
  # Я не совсем разобрался с мемоизацией, т.к не совсем разобрался с декоратарами, но принцип работы понятен.
  # Нашёл готовое решение в стандартной библиотеке. 
from functools import lru_cache
from timeit import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@lru_cache()
def recursive_reverse_1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

print(timeit("recursive_reverse(345923459832459263459723465879342563457986)", "from __main__ import recursive_reverse"))
print(timeit("recursive_reverse_1(345923459832459263459723465879342563457986)", "from __main__ import recursive_reverse_1"))