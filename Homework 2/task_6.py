"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random
def number_f(number = 0, counter = 0):
    if counter == 0:
        number = random.randint(0, 100)
    if counter == 10:
        print(f"Loose, the number was {number}")
        return
    user = input("Enter your number: ")
    if int(user) == number:
        print("Win")
        return
    if int(user) > number:
        print("Youy number is greater!")
    if int(user) < number:
        print("Youy number is less!")
    number_f(number, counter+1,)
number_f()