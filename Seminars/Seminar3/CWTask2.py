# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random
import os

path = "Seminars\Seminar3\CWT2_input_data.txt"

def fill_list(n):
    list = []
    for i in range(0, n):
        list.append(random.randint(-n, n))
    return list
    
def read_file():
    file = open(path, "r")
    list = []
    for line in file:
        list.append(int(line))
    file.close()
    return list

def multi_on_pos(list, pos):
    result = 1
    for i in range(0, len(list)):
        result *= list[i]
    return result

def main():
    n = int(input("Ведите N: "))
    list = fill_list(n)
    print(list)
    positions = read_file()
    print(positions)
    print("Произведение элементов на указанных позициях: ", multi_on_pos(list, positions))

if __name__ == "__main__":
    main()
