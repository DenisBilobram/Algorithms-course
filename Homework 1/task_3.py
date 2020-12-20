"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
# 1.1 решение циклом, нахожу большее, удаляю, и так 3 раза.
# по скорости решение должно быть довольно эффективным.
# Сложность: O(n)
def top_three_first(dictionary):
    top = []
    for i in range(3):
        first = list(dictionary.values())[0]
        for key in dictionary:
            if dictionary[key] >= first:
                first = dictionary[key]
                first_key = key
        del dictionary[first_key]
        top.append(first_key)
    return top


# 1.2 решение рекурсией. 
# по скорости решения одинаковые. ничего более не придумал.
# Сложность: O(n)
def top_g(dictionary, result=[]):
    first = list(dictionary.values())[0]
    for key in dictionary:
        if dictionary[key] >= first:
            first = dictionary[key]
            first_key = key
    result.append(dictionary[first_key])
    del dictionary[first_key]
    if len(result) == 3:
        return result
    return top_g(dictionary)