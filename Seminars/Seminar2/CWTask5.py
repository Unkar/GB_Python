# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

from itertools import count


string_short = input("Введите первую строку: ")
string_long = input("Введите вторую строку: ")

counter = 0

for i in range(len(string_long)):
    if string_short == string_long[i:i+len(string_short)]:
        counter += 1

print(counter)

        