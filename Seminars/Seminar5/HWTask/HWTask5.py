# задача 5 необязательная Дан список чисел.
#  Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
#  Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 

#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
from msilib import sequence
import random
def generate_list(list_length, min_value, max_value):
    return [random.randint(min_value, max_value) for i in range(list_length)]

def clear_repeats(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result

def find_all_sequences(list):
    sequences = []
    sequence = []
    for i in range(len(list)):
        if i == 0:
            sequence.append(list[i])
        elif list[i] == list[i-1] + 1:
            sequence.append(list[i])
            if i == len(list) - 1:
                sequences.append(sequence)
        else:
            sequences.append(sequence)
            sequence = []
            sequence.append(list[i])
    return sequences

def find_longest_sequence(list):
    sequences = find_all_sequences(list)
    max_sequence = []
    for sequence in sequences:
        if len(sequence) > len(max_sequence):
            max_sequence = sequence
    return max_sequence

def main():
    list_length = 20
    min_value = 1
    max_value = 20
    list = generate_list(list_length, min_value, max_value)
    print("Исходный список:" + str(list))
    list = sorted(list)
    list = clear_repeats(list)
    print("Все найденные последовательности:" + str(find_all_sequences(list)))
    print("Самая длинная последовательность:" + str(find_longest_sequence(list)))
    result = find_longest_sequence(list)
    print ([result[0], result[-1]])
    return [result[0], result[-1]]
    

if __name__ == "__main__":
    main()