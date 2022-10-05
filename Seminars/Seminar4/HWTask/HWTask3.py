# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

def get_polynomial(k):
    return [random.randint(0, 100) for i in range(k + 1)]

def create_string(k, polynomial):
    string = ""
    for i in range(k, -1, -1):
        if i == 0:
            string += str(polynomial[i])
        elif i == 1:
            string += str(polynomial[i]) + "*x + "
        else:
            string += str(polynomial[i]) + "*x^" + str(i) + " + "
    string += " = 0"
    return string

def main():
    k = int(input("Enter a natural number: "))
    polynomial = get_polynomial(k)
    string = create_string(k, polynomial)
    print(string)
    with open("Seminars/Seminar4/HWTask/polynomial.txt", "w") as file:
        file.write(string)    

if __name__ == "__main__":
    main()

