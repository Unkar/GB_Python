# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def get_fractional_part(number):
    return number - int(number)

def get_integer_part(number):
    return int(number)

def get_fractional_count_digits(number):
    count = 0
    while number != int(number):
        number *= 10
        count += 1
    return count

def sum_digits(number, count=0):
    if number < 0:
        number = -number
    sum = 0
    if number > 1:
        while number > 0:
            sum += number % 10
            number = number // 10
    else:
        for i in range(count):
            number *= 10
            sum += int(number % 10)
    return sum

def main():
    number = float(input("Введите число: "))
    fractional_part = get_fractional_part(number)
    integer_part = get_integer_part(number)
    print("количество цифр в дробной части: ", get_fractional_count_digits(number))
    print(f"Целая часть: {integer_part}")
    print(f"сумма цифр целой части: {sum_digits(integer_part)}")
    print(f"Дробная часть: {fractional_part}")
    print(f"сумма цифр дробной части: {sum_digits(fractional_part, get_fractional_count_digits(number))}")
    print(f"Сумма цифр числа: {sum_digits(integer_part) + sum_digits(fractional_part, get_fractional_count_digits(number))}")
    # print(sum_digits(number))   

if __name__ == "__main__": #Запуск программы если файл запущен как основной
    main()