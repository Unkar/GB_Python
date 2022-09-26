# Задача 3. Реализуйте алгоритм перемешивания списка.
#  Список размерностью 10 задается случайными целыми числами,
#  выводится на экран, затем перемешивается, опять выводится на экран.

import random

def generate_list(size):
    result_list = []
    for i in range(size):
        result_list.append(random.randint(0, 100))
    return result_list

def shuffle_list(list):
    for i in range(len(list)):
        j = random.randint(0, len(list) - 1)
        list[i], list[j] = list[j], list[i]
    return list

def main():
    size = 10
    list = generate_list(size)
    print(list)
    print(shuffle_list(list))

if __name__ == "__main__": #Запуск программы если файл запущен как основной
    main()