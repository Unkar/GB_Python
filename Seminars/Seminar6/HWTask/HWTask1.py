# Задача 1. Создайте программу для игры в "Крестики-нолики".

field_size=4


def create_field(field_size):
    array = []
    for i in range(field_size):
        array.append([])
        if i == 0:
            array[i] = [j for j in range(field_size)]
        else:  
            array[i] = ["." for j in range(field_size)]
            array[i][0] = i
    return array


def print_field(field):
    for i in range(field_size):
        for j in range(field_size):
            print(field[i][j], end=" ")
        print()

def check_win():
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2]:
            return True
        if array[0][i] == array[1][i] == array[2][i]:
            return True
    if array[0][0] == array[1][1] == array[2][2]:
        return True
    if array[0][2] == array[1][1] == array[2][0]:
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if array[i][j] != "X" and array[i][j] != "O":
                return False
    return True

def check_input(x, y, field_size):
    if x < 1 or x > field_size - 1:
        return False
    if y < 1 or y > field_size - 1:
        return False
    return True

def make_move(x, y, player):
    array[x][y] = player

def game():
    print("Игра крестики-нолики")
    print("Введите координаты хода в формате x y")
    print("x - номер строки, y - номер столбца")
    print("Начинает игрок с крестиками")
    print_field(array)
    player = "X"
    while True:
        print("Ходит крестики" if player == "X" else "Ходит нолики")
        x, y = map(int, input().split())
        if not check_input(x, y, field_size):
            print("Некорректный ввод")
            continue
        if array[x][y] != ".": 
            print("Клетка занята")
            continue
        make_move(x, y, player)
        print_field(array)
        if check_win():
            print("Победили крестики" if player == "X" else "Победили нолики")
            break
        if check_draw():
            print("Ничья")
            break
        player = "X" if player == "O" else "O"

def main():
    global array
    array = create_field(field_size)
    game()

if __name__ == "__main__":
    main()