# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def calc(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        if y == 0:
            return "Деление на 0!"
        else:
            return x / y
    elif operator == "*":
        return x * y
    elif operator == "mod":
        if y == 0:
            return "Деление на 0!"
        else:
            return x % y
    elif operator == "pow":
        return x ** y
    elif operator == "div":
        if y == 0:
            return "Деление на 0!"
        else:
            return x // y
    else:
        return "Неверный оператор"

def main():
    try:
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        operator = input("Введите оператор: ")
        print(calc(x, y, operator))
    except:
        print("Неверный ввод")