# from random import randint, random

# import random


# def create_2d_array(rows, columns):
#     int_Array = []
#     for i in range(rows):
#         int_Array.append([])
#         for j in range(columns):
#             int_Array[i].append(0)
#     return int_Array


# def fill_random_2d_array(int_Array):
#     for i in range(len(int_Array)):
#         for j in range(len(int_Array[i])):
#             int_Array[i][j] = input(randint(0, 100))
#     return int_Array


# def print_2d_array(int_Array):
#     for i in range(len(int_Array)):
#         for j in range(len(int_Array[i])):
#             print(int_Array[i][j], end=' ')
#         print()

# def sort_array_by_rows(int_Array):
#     for i in range(len(int_Array)):
#         for j in range(len(int_Array[i])):
#             for k in range(len(int_Array[i]) - 1):
#                 if int_Array[i][k] > int_Array[i][k + 1]:
#                     int_Array[i][k], int_Array[i][k + 1] = int_Array[i][k + 1], int_Array[i][k]
#     return int_Array

# def sort_array_by_columns(int_Array):
#     for i in range(len(int_Array)):
#         for j in range(len(int_Array[i])):
#             for k in range(len(int_Array) - 1):
#                 if int_Array[k][j] > int_Array[k + 1][j]:
#                     int_Array[k][j], int_Array[k + 1][j] = int_Array[k + 1][j], int_Array[k][j]
#     return int_Array

# def print_2d_array(int_Array):
#     for i in range(len(int_Array)):
#         for j in range(len(int_Array[i])):
#             print(int_Array[i][j], end=' ')
#         print()

# try:
#     rows = int(input("Введите количество строк: "))
#     columns = int(input("Введите количество столбцов: "))
#     int_Array = create_2d_array(rows, columns)
#     int_Array = fill_random_2d_array(int_Array)
#     print_2d_array(int_Array)
#     int_Array = sort_array_by_rows(int_Array)
#     int_Array = sort_array_by_columns(int_Array)
#     print_2d_array(int_Array)
# except:
#     print("Неверный ввод")