# 20. Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.

import re


list = ['42','35','34']

def find_number(list, number):
    result = False
    for i in list:
        if i == str(number):
            result = True
    return result

def main():
    try:
        number = input('Введите число: ')
        print('Присутствие числа в списке:', find_number(list,number))
    except:
        print('Неверный ввод!')

main()
