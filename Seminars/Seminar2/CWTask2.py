# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

import random

N = int(input("Введите число N: "))

def sequence(N):
    list = []
    for i in range(N):
        list.append((-1)**i*3**i)
    return list

def print_list(list):
    for i in range(len(list)-1):
        print(list[i], end=", ")
    print(list[i])
    print()

print_list(sequence(N))