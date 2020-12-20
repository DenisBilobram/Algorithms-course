"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

# По результатам профилирования видно, что revers_3 наиболее эффективный алгоритм.
# В revers_3 не используются ни цикл, ни рекурсия, что делает его наиболее быстрым.

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    print(revers(123456780))
    print(revers_2(123456780))
    print(revers_3(123456780))

cProfile.run('main()')

print("Revers   " + str(timeit("revers(1234567890)", "from __main__ import revers", number = 10000)))
print("Revers_2 " + str(timeit("revers_2(1234567890)", "from __main__ import revers_2", number = 10000)))
print("Revers_3 " + str(timeit("revers_3(1234567890)", "from __main__ import revers_3", number = 10000)))