list = input("Введите числа через запятую: ").split(",")

def findMaxBubble(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if int(list[j]) > int(list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list[-1]

print(findMaxBubble(list))
