# Задача 1 Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def generate_list(quantity):
    list = []
    for i in range(quantity):
        list.append(random.randint(0, 100))
    return list

def sum_odd(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum

def main():
    quantity = int(input("Введите количество элементов списка: "))
    list = generate_list(quantity)
    print("Список:", list)
    print("Сумма элементов списка, стоящих на нечётных позициях:", sum_odd(list))

main()
