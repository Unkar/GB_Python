a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def check(a, b):
    if a == b**2:
        print("Первое число является квадратом второго")
    elif b == a**2:
        print("Второе число является квадратом первого")
    else:
        print("Ни одно число не является квадратом другого")

check(a, b)
