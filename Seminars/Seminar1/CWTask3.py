from random import randint, random

import random


def create_2d_array(rows, columns):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(columns):
            array[i].append(0)
    return array


def fill_random_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = input(randint(0, 100))
    return array


def print_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=' ')
        print()


try:
    rows = int(input("Введите количество строк: "))
    columns = int(input("Введите количество столбцов: "))
    array = create_2d_array(rows, columns)
    array = fill_random_2d_array(array)
    print_2d_array(array)
except:
    print("Неверный ввод")
