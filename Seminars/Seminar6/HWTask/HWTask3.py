# Задача FOOTBALL необязательная: Напишите программу, которая принимает на стандартный вход
#  список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

PATH = "Seminars/Seminar6/HWTask/football.txt"

# def open_file():
#     with open(PATH, 'r', encoding = 'utf-8') as file:
#         games = []
#         for line in file:
#             games.append(line.split(';'))
#     return games

def input_games():
    games = []
    while True:
        game = input('Введите результаты игры в формате: Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой:(показать таблицу - пустая строка):')
        if game == '':
            break
        games.append(game.split(';'))
    return games
    
def get_commands(games):
    commands = []
    for game in games:
        if game[0] not in commands:
            commands.append(game[0])
        if game[2] not in commands:
            commands.append(game[2])
    commands.sort()
    return commands

def get_results(games, commands):
    commands_results = {}
    for command in commands:
        commands_results[command] = [0, 0, 0, 0, 0]
    for game in games:
        if int(game[1]) > int(game[3]):
            commands_results[game[0]][0] += 1
            commands_results[game[0]][1] += 1
            commands_results[game[0]][4] += 3
            commands_results[game[2]][0] += 1
            commands_results[game[2]][3] += 1
        elif int(game[1]) < int(game[3]):
            commands_results[game[2]][0] += 1
            commands_results[game[2]][1] += 1
            commands_results[game[2]][4] += 3
            commands_results[game[0]][0] += 1
            commands_results[game[0]][3] += 1
        else:
            commands_results[game[0]][0] += 1
            commands_results[game[0]][2] += 1
            commands_results[game[0]][4] += 1
            commands_results[game[2]][0] += 1
            commands_results[game[2]][2] += 1
            commands_results[game[2]][4] += 1
    return commands_results

def print_results(commands_results):
    print('Команда:Всегоигр Побед Ничьих Поражений Всегоочков')
    for command in commands_results:
        print(command + ':', end = ' ')
        for result in commands_results[command]:
            print(result, end = ' ')
        print()

def main():
    # games = open_file()
    games = input_games()
    print(games)
    commands = get_commands(games)
    print(commands)
    commands_results = get_results(games, commands)
    print(commands_results)
    print_results(commands_results)

if __name__ == '__main__':
    main()



