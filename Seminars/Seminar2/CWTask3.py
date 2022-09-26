import random

n = int(input("Введите число N (размерность пространства): "))

def generate_random_point(N):
    point = []
    for i in range(N):
        point.append(random.randint(-100,100))
    return point

def distance(A,B):
    sum = 0
    for i in range(len(A)):
        sum += (A[i]-B[i])**2
    return sum**0.5

a = generate_random_point(n)    
b = generate_random_point(n)
print(f"Сгенерирована точка А: {a}")
print(f"Сгенерирована точка B: {b}")
print(f"Расстояние между точками А и B: {distance(a,b)}")