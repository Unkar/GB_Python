# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  Количество предикат генерируется случайным образом от 5 до 11,
#  проверяем это утверждение 10 раз, с помощью модуля time выводим на экран ,
#  сколько времени отработала программа.

# Решил сделать так, чтобы работало для любого количества предикатов.
# Я создаю двумерный массив, в котором будут храниться все возможные комбинации предикатов.
#пример для 3 предикатов
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# Потом я просто проверяю утверждение для каждой комбинации.
# Выводится на экран результат проверки утверждения для каждой комбинации.
# Классная задача, спасибо за неё.

import random
import time

#делаем чек лист предикатов для проверки
def check_list_predicate(number):
    array = []
    for i in range(2**number):  # вариантов всего 2 в степени количества предикатов
        array.append([])
        array[i] = list(bin(i)[2:].zfill(number)) #добавляем в массив бинарное представление числа, добавляем нули в начало и разбиваем на символы
    return array

#проверяем значение левой части утверждения
def first_expression(array):
    result = bool(None)
    for i in range(len(array)):
        result = result or array[i]
    return not result

#проверяем значение правой части утверждения
def second_expression(array):
    result = bool(None)
    for i in range(len(array)):
        result = result and not array[i]
    return result

#проверяем утверждение
def check_statement(array):
    return first_expression(array) == second_expression(array)

#функция для вывода листа предикатов и результатов проверки утверждения
def print_check_statement(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(bool(int(array[i][j])), end=' ')
        print(f" -> {check_statement(array[i])}")

def main():
    number = random.randint(5, 11)
    array = check_list_predicate(number)
    for i in range(10):
        print(f"Проверка №{i+1}")
        print_check_statement(array)
        print()
    print(f"Количество предикатов: {number}")
    print(f"Время выполнения программы: {time.process_time()} секунд")
    
if __name__ == '__main__':
    main()

