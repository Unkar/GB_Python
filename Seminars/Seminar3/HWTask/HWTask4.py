# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]

def main():
    try:
        decimal = int(input("Введите десятичное число: "))
        print("Двоичное число:", decimal_to_binary(decimal))
    except:
        print("Ошибка ввода!")

main()
