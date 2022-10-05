#задача 2 . Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.

def getUniqueElements(seq):
    unique = []
    for i in seq:
        if i not in unique:
            unique.append(i)
    return unique

def main():
    seq = [1, 2, 3, 18, 5, 17, 7, 8, 9, 10, 1, 2, 3, 23, 5, 6, 47, 8, 9, 10]
    unique = getUniqueElements(seq)
    print(unique)

if __name__ == "__main__":
    main()