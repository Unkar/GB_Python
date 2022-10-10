# 1 2 3
# 4 5 6
# 7 8 9

# 00  01  02
# 10  11  12
# 20  21  22

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

field_index = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (
    1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}


def print_field(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()


def make_move(player, move, field):
    coords = field_index[move]
    if field[coords[0]][coords[1]] == "X" or field[coords[0]][coords[1]] == "O":
        print("Неверный ход")
        return
    if player == 1:
        field[coords[0]][coords[1]] = "X"
    else:
        field[coords[0]][coords[1]] = "O"
    

def who_win(char):
    if char == "X":
        return 1
    else:
        return 2


def check_win(field):
    for i in range(len(field)):
        if field[i][0] == field[i][1] == field[i][2]:
            return who_win(field[i][0])
        if field[0][i] == field[1][i] == field[2][i]:
            return who_win(field[0][i])
    if field[0][0] == field[1][1] == field[2][2]:
        return who_win(field[0][0])
    if field[0][2] == field[1][1] == field[2][0]:
        return who_win(field[0][2])
    return 0

def game():
    field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_field(field)
    player = 1
    while True:
        move = int(input("Ход игрока " + str(player) + ": "))
        make_move(player, move, field)
        print_field(field)
        if check_win(field) != 0:
            print("Игрок", check_win(field), "победил")
            break
        if player == 1:
            player = 2
        else:
            player = 1


game()