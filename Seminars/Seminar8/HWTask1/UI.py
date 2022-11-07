import easygui
import json_request
import error_handler
from main import session_id as id

global session_id 
session_id = id
#Стартовое окно
#1. Вход
#2. регистрация
#3. выход

def start_window():
    msg = "Выберите действие"
    title = f"Вход. Сессия {session_id}"
    choices = ["Вход", "Регистрация", "Выход", "Показать логи"]
    choice = easygui.buttonbox(msg, title, choices)
    return choice

#Вход
#1. Ввод логина
#2. Ввод пароля
#3. Регистрация
#4. Выход

def entrance_window():
    msg = "Введите логин и пароль"
    title = f"Вход. Сессия {session_id}"
    fieldNames = ["Логин", "Пароль"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multpasswordbox(msg, title, fieldNames)
    return fieldValues

#Регистрация
#1. Ввод логина
#2. Ввод пароля
#3. Ввод пароля повторно
#4. Фамилия
#5. Имя
#6. Отчество
#7. N телефона
#8. E-mail
#9. Статус
#10. Выход

def registration_window():
    msg = "Заполните поля"
    title = f"Регистрация. Сессия {session_id}"
    fieldNames = ["Логин", "Пароль", "Повторите пароль", "Фамилия", "Имя", "Отчество", "Дата рождения","Номер телефона", "E-mail", "Коротко о себе"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    return fieldValues

def status_window():
    msg = "Выберите статус"
    title = f"Регистрация. Сессия {session_id}"
    choices = ["холост/не замужем", "женат/замужем", "в разводе", "вдовец/вдова", "в активном поиске"]
    choice = easygui.buttonbox(msg, title, choices)
    return choice


#Главное меню
#1. Посмотреть список пользоватеелей.
#2. Посмотреть кто смотрит вас.
#3. Посмотреть кого смотрели вы.
#4. Посмотреть пользователя
#4. выход

def main_menu_window(user_id):
    msg = "Выберите действие"
    title = f"Главное меню. Сессия {user_id}"
    choices = ["Посмотреть список пользователей", "Посмотреть кто смотрел мой профиль", "Посмотреть кого смотрели вы", "Выход"]
    choice = easygui.buttonbox(msg, title, choices)
    return choice

#Просмотр списка пользователей
def users_list_window(user_list):
    msg = "Выберите пользователя"
    title = f"Список пользователей. Сессия {session_id}"
    choice = easygui.choicebox(msg, title, user_list)
    return choice


def show_user_info_window(user_info):
    msg = "Информация о пользователе"
    title = f"Информация о пользователе. Сессия {session_id}"
    easygui.msgbox(msg, title, user_info)

def error_window(error):
    title = "Ошибка"
    easygui.msgbox(str(error), title)