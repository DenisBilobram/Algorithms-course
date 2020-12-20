"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
# Решил своим способом без сортировки.
from statistics import median
from random import randint
lst = [randint(0, 100) for el in range(2 * int(input("Enter m: ")) + 1)]

for el in lst:
    count = 0
    for i in lst:
        if el >= i:
            count += 1
        if el <= i:
            count -= 1
    if count == 0:
            med = el
            break
            
print(med)
print(median(lst))

