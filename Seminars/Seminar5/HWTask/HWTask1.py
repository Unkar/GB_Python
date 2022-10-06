# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# от себя добавил уровень сложности бота.

import random


def main_menu():
    print("-"*50+"\n1. Играть против бота")
    print("2. Играть против друга")
    print("3. Выход\n"+"-"*50)
    while True:
        try:
            choice = int(input("Выберите пункт меню: "))
            print("-" * 50)
            if choice not in [1, 2, 3]:
                print("Нет такого пункта меню")
                continue
            return choice
        except ValueError:
            print("Введите число")
            continue


def game(player1, player2, number_of_candies, lvl=1, max_candies=28):
    while number_of_candies > 0:
        print_table(number_of_candies)
        if player1 == "Бот":
            candies = bot_candies(number_of_candies, lvl, max_candies)
            print("Бот взял", candies, "конфет")
        else:
            candies = get_candies(player1, number_of_candies)
        number_of_candies -= candies
        if number_of_candies == 0:
            print("-"*50 + "\nИгрок", player1, "победил\n" + "-"*50)
            break
        print_table(number_of_candies)
        if player2 == "Бот":
            candies = bot_candies(number_of_candies, lvl, max_candies)
            print("Бот взял", candies, "конфет")
        else:
            candies = get_candies(player2, number_of_candies)
        number_of_candies -= candies
        if number_of_candies == 0:
            print("Игрок", player2, "победил")


def bot_candies_hard_lvl(number_of_candies, max_candies=28):
    if number_of_candies % (max_candies+1) == 0:
        return max_candies
    else:
        return number_of_candies % (max_candies+1)


def bot_candies_mid_lvl(number_of_candies, max_candies=28):
    when_bot_become_smarter = 10
    if number_of_candies <= max_candies * when_bot_become_smarter:
        return bot_candies_hard_lvl(number_of_candies, max_candies)
    else:
        return bot_candies_easy_lvl(max_candies)


def bot_candies_easy_lvl(max_candies=28):
    return random.randint(1, max_candies)


def bot_candies(number_of_candies, lvl, max_candies=28):
    if lvl == 1:
        return bot_candies_easy_lvl(max_candies)
    elif lvl == 2:
        return bot_candies_mid_lvl(number_of_candies, max_candies)
    elif lvl == 3:
        return bot_candies_hard_lvl(number_of_candies, max_candies)


def print_table(number_of_candies):
    print("-"*50 + "\nКонфет на столе:", number_of_candies, "\n" + "-"*50)


def get_candies(player, number_of_candies):
    while True:
        try:
            candies = int(input("Игрок " + str(player) +
                          " введите количество конфет: "))
            if candies > 28:
                print("Вы не можете взять больше 28 конфет за один ход")
                continue
            if candies > number_of_candies:
                print("На столе нет столько конфет")
                continue
            return candies
        except ValueError:
            print("Введите число")
            continue


def get_name_of_player(number_of_player):
    return input("Введите имя игрока " + str(number_of_player) + ": ")


def get_lvl_of_bot():
    while True:
        try:
            lvl = int(
                input("Выберите уровень сложности бота (1-легкий, 2-средний, 3-сложный): "))
            if lvl not in [1, 2, 3]:
                print("Нет такого уровня сложности")
                continue
            return lvl
        except ValueError:
            print("Введите число")
            continue


def who_first(player1, player2):
    if random.randint(1, 2) == 1:
        print("Игрок", player1, "ходит первым")
        return player1, player2
    else:
        print("Игрок", player2, "ходит первым")
        return player2, player1


def main():
    start_number_of_candies = 100
    max_pieces_of_candies = 28
    while True:
        choice = main_menu()
        if choice == 1:
            lvl_of_bot = get_lvl_of_bot()
            player1, player2 = who_first("Бот", get_name_of_player(1))
            game(player1, player2, start_number_of_candies,
                 lvl_of_bot, max_pieces_of_candies)
        elif choice == 2:
            player1, player2 = who_first(
                get_name_of_player(1), get_name_of_player(2))
            game(player1, player2, start_number_of_candies, max_pieces_of_candies)
        else:
            break


if __name__ == "__main__":
    main()
