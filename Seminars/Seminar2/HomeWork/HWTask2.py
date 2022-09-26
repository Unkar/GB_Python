# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))
result_list = []
for i in range(1, number + 1):
    result = 1
    for j in range(1, i + 1):
        result *= j
    result_list.append(result)

print(result_list)
