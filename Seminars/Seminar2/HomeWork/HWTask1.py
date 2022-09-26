# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
def sum_digits(number):
    sum = 0
    if number < 0:
        number = -number

    number_before_dot = round(number)
    number_after_dot = number - number_before_dot

    while number_before_dot > 0:
        sum += number_before_dot % 10
        print(number_before_dot % 10)
        number_before_dot //= 10

    while number_after_dot != 0:
        number_after_dot *= 10
        sum += round(number_after_dot)
        number_after_dot -= round(number_after_dot)
    return sum

def main():
    number = float(input("Введите число: "))
    print(sum_digits(number))   

if __name__ == "__main__": #Запуск программы если файл запущен как основной
    main()