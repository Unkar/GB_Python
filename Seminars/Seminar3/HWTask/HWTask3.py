# Задача 3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def generate_double_list(quantity):
    list = []
    for i in range(quantity):
        list.append(round(random.random() * 100, 2))
    return list

def find_max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

def find_min(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

def difference_max_min_fractional_part(list):
    max = find_max(list)
    min = find_min(list)
    result = round((max % 1 - min % 1), 2)
    return result

def main():
    try:
        quantity = int(input("Введите количество элементов списка: "))
        list = generate_double_list(quantity)
        print("Список:", list)
        print("Разница между максимальным и минимальным значением дробной части элементов:", difference_max_min_fractional_part(list))
    except:
        print("Ошибка ввода!")

main()    