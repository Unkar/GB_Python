#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 

def check_weekend_day(day_of_week):
    while day_of_week > 7 or day_of_week < 1:
        day_of_week = int(input("Такого дня недели нет. Введите число от 1 до 7: "))
    if day_of_week == 6 or day_of_week == 7:
        return True
    else:
        return False

def main():
    try:
        day_of_week = int(input("Введите цифру от 1(Пн) до 7(Вс) обозначающую день недели: "))
        if check_weekend_day(day_of_week):
            print("Да")
        else:
            print("Нет")
    except:
        print("Неверный ввод")   
