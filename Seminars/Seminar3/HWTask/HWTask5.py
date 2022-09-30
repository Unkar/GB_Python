# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
#  причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
#  Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился
#  на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
#  то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random

def generate_int_2d_array(m, n):
    array = []
    for i in range(m):
        array.append([])
        for j in range(n):
            array[i].append(random.randint(0, 10))
    return array

def print_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()

def convert_2d_array_to_list(array):
    list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            list.append(array[i][j])
    return list

def convert_list_to_2d_array(list, m, n):
    array = []
    for i in range(m):
        array.append([])
        for j in range(n):
            array[i].append(list[i * n + j])
    return array

def shuffle_2d_array(array):
    list = convert_2d_array_to_list(array)
    index_list = [x for x in range(len(list))]
    for i in range(len(list) // 2):
        rnd_indx1 = random.choice(index_list)
        index_list.remove(rnd_indx1)
        rnd_indx2 = random.choice(index_list)
        index_list.remove(rnd_indx2)
        list[rnd_indx1], list[rnd_indx2] = list[rnd_indx2], list[rnd_indx1]
    return convert_list_to_2d_array(list, len(array), len(array[0]))

def check_dimensions(m, n):
    if m * n % 2 == 0:
        return True
    else:
        return False    

def main():
    try:
        while True:
            m = int(input("Введите m: "))
            n = int(input("Введите n: "))
            if check_dimensions(m, n):
                break
            else:
                print("Количество элементов должно быть четным!")
        array = generate_int_2d_array(m, n)
        print("Исходный массив:")
        print_2d_array(array)
        print("Перемешанный массив:")
        print_2d_array(shuffle_2d_array(array))
    except:
        print("Ошибка ввода!")

main()
