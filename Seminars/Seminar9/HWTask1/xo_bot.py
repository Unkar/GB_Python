#оболочка телеграм бота для крестиков-ноликов
import telebot
import random
import main

TOKEN = '5628275281:AAFJkOxs_IRBE4f35QxbC6AaaZAz5haCw7s'
#подключаем библиотеку для работы с телеграм ботом
bot = telebot.TeleBot('token')

#приветствие
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который умеет играть в крестики-нолики. Напиши мне /play, чтобы начать игру.')

#игра
@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, 'Начинаем игру!')
    bot.send_message(message.chat.id, 'Я ходю первый, выбери номер клетки, куда поставить крестик (от 1 до 9).')
    bot.send_message(message.chat.id, '1|2|3\n4|5|6\n7|8|9')
    bot.register_next_step_handler(message, play_step)

#ход игрока
def play_step(message):
    if message.text.isdigit() and int(message.text) in range(1, 10):
        field = main.Field()
        field.set_cell(int(message.text), main.Cell.X)
        bot.send_message(message.chat.id, 'Твой ход:\n' + field.get_field())
        if field.check_win(main.Cell.X):
            bot.send_message(message.chat.id, 'Ты выиграл!')
        elif field.is_full():
            bot.send_message(message.chat.id, 'Ничья!')
        else:
            bot.send_message(message.chat.id, 'Мой ход:')
            field.set_cell(main.get_computer_move(field), main.Cell.O)
            bot.send_message(message.chat.id, field.get_field())
            if field.check_win(main.Cell.O):
                bot.send_message(message.chat.id, 'Я выиграл!')
            elif field.is_full():
                bot.send_message(message.chat.id, 'Ничья!')
            else:
                bot.send_message(message.chat.id, 'Выбери номер клетки, куда поставить крестик (от 1 до 9).')
                bot.register_next_step_handler(message, play_step)
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод, попробуй еще раз.')
        bot.register_next_step_handler(message, play_step)

bot.polling()


