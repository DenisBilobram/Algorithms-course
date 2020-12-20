"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
#  За основу алгоритма брал чужой код, сам придумать не смог.
import random

def merge_sort(array):
    if len(array) <= 1:
        return array
    midpoint = len(array) // 2
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

count = input("Введите число элементов: ")
lst = [random.uniform(0, 49) for el in range(0, int(count))]
print(lst)
print(merge_sort(lst))
