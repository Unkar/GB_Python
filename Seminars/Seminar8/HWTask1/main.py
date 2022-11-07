import UI
import json_request
import error_handler
import log
import re

global session_id
session_id = None


def start():
    try:
        while True:
            choice = UI.start_window()
            if choice == "Вход":
                entrance()
            elif choice == "Регистрация":
                registration()
            elif choice == "Выход" or choice == None:
                break
            elif choice == "Показать логи":
                log.show_log()
            else:
                error_handler.error_window(
                    f"Ошибка в start_window. Выбрано: {choice}")

    except Exception as e:
        error_handler.error_window(e, session_id)


def entrance():
    try:
        log_pass = UI.entrance_window()
        if log_pass != None:
            # Проверка логина и пароля
            if json_request.check_login(log_pass[0], log_pass[1]):
                general(json_request.get_user_id(log_pass[0]))
            else:
                error_handler.error_window("Неверный логин или пароль")
        else:
                registration()
    except Exception as e:
        error_handler.error_window(e, session_id)


def registration():
    try:
        while True:
            log_pass = UI.registration_window()
            if log_pass != None:
                # Проверка логина и пароля
                if json_request.check_login(log_pass[0]):
                    error_handler.error_window("Такой логин уже существует")
                else:
                    # Регистрация
                    log_pass.append(UI.status_window())
                    general(json_request.registration(log_pass))
            else:
                break
    except Exception as e:
        error_handler.error_window(e, session_id)


def profile(user_id):
    try:
        user_info_dict = json_request.get_user_info(user_id)
        user_info_string = ""
        for key in user_info_dict:
            user_info_string += key + ": " + user_info_dict[key] + "\n"
        UI.show_user_info_window(user_info_string)
    except Exception as e:
        error_handler.error_window(e, session_id)


def general(user_id):
    try:
        global session_id
        session_id = user_id
        choice = UI.main_menu_window(user_id)
        person = ""
        if choice == "Посмотреть список пользователей":
            person = UI.users_list_window(json_request.get_users())
        elif choice == "Посмотреть кто смотрел мой профиль":
            person = UI.users_list_window(log.get_viewers(user_id))
        elif choice == "Посмотреть кого смотрели вы":
            person = UI.users_list_window(log.get_viewed(user_id))
        elif choice == "Выход":
            return
        else:
            error_handler.error_window(
            "Ошибка в main_menu_window", session_id)
        if person != None:
                # Просмотр профиля c обрезанием UID
                profile(person[:person.find(":::")].strip())
                # Добавление в просмотренные
                log.add_viewed(user_id, person)
    except Exception as e:
        error_handler.error_window(e)


if __name__ == "__main__":
    start()
