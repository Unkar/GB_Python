#задача 4. Задайте два числа. Напишите программу,
#которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def get_nok(a, b):
    if a > b:
        a, b = b, a
    for i in range(1, b + 1):
        if (a * i) % b == 0:
            return a * i

def main():
    a = int(input("Enter a natural number: "))
    b = int(input("Enter a natural number: "))
    print(get_nok(a, b))

if __name__ == "__main__":
    main()