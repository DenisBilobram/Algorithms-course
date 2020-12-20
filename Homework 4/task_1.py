"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
  # Я написал решение генератором списков. Он работает быстрее т.к не создаются ненужные перменные, 
  # не вызываются дополнительные функции и т.д.

from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return [el for el in nums if el % 2 == 0]


print("Test first " + str(timeit("func_1([el for el in range(0, 1000)])", "from __main__ import func_1", number = 1000)))
print("Test second " + str(timeit("func_2([el for el in range(0, 1000)])", "from __main__ import func_2", number = 1000)))
