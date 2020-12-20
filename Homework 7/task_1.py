"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from timeit import timeit
from random import randint

def bubble_sort(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

def bubble_sort_opt(lst):
    for j in range(len(lst)):
        lst_c = lst.copy()
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if lst_c == lst:
            return lst
    return lst

lst = [randint(-100, 100) for el in range(-100, 100)]
print(f"Before: {lst}\nAfter: {bubble_sort_opt(lst)}\n")

print("Test first " + str(timeit("bubble_sort(lst)", "from __main__ import bubble_sort, lst", number = 1000)))
print("Test second " + str(timeit("bubble_sort_opt(lst)", "from __main__ import bubble_sort_opt, lst", number = 1000)))

# Тесты показывают, что вариант сортировки пузырьком с оптимизацией работает гораздо быстрее.