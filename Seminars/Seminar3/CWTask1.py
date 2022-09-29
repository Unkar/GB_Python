#  16. Задайте список из n чисел последовательности (1 + 1/n)*n  и выведите на экран их сумму.

def sequence(n):
    return (1 + 1/n)*n

def feel_list(n):
    list = []
    for i in range(1, n+1):
        list.append(sequence(i))
    return list

def sum(n):
    list = feel_list(n)
    sum = 0
    for i in list:
        sum += i
    return sum

def main():
    n = int(input("Enter n: "))
    print("Sum of sequence: ", sum(n))

if __name__ == "__main__":
    main()
    