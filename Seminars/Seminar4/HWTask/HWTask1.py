#задача 1. Задайте натуральное число N.
#Напишите программу, которая составит список простых множителей числа N.

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def getPrimeFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0 and isPrime(i):
            factors.append(i)
    return factors

def main():
    n = int(input("Enter a number: "))
    factors = getPrimeFactors(n)
    print(factors)

if __name__ == "__main__":
    main()
                    