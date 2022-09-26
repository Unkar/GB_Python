# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
import random

def generate_2d_random_array(rows, columns):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(columns):
            array[i].append(random.randint(0, 100))
    return array


def print_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()


def align_array(array):
    aligned_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            aligned_array.append(array[i][j])
    return aligned_array


def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def return_2d_array(list, rows, columns):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(columns):
            array[i].append(list[i * columns + j])
    return array

def sort_2d_array(array):
    aligned_array = align_array(array)
    sort_list(aligned_array)
    sorted_array = return_2d_array(aligned_array, len(array), len(array[0]))
    return sorted_array

def main():
    try:
        row = int(input("Введите количество строк: "))
        column = int(input("Введите количество столбцов: "))
        array = generate_2d_random_array(row, column)
        print("Исходный массив:")
        print_2d_array(array)
        sorted_array = sort_2d_array(array)
        print("Отсортированный через список массив:")
        print_2d_array(sorted_array)
        sorted_array = sort_2d_array_by_sort(array)
    except:
        print("Неверный ввод")

main()
