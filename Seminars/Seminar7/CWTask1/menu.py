from datetime import date
import errhandling as err
import config as cfg


def main_menu():
    """Основное меню калькулятора"""
    menu_items = 3
    while True:
        print(""""Главное меню:
        1. Запустить калькулятор
        2. Настройки калькулятора
        3. Выход""")
        value = input("Введите номер пункта меню: ")
        if not err.check_menu_error(value, menu_items):
            break
    return value


def settings_menu():
    status = cfg.history_recording_status
    status_error = cfg.history_error_visiable_status
    """Меню настроек"""
    menu_items = 6
    while True:
        print(f""""Настройки:
        1. {'Включить' if not status else 'Выключить'} запись истории вычислений
        2. {'Включить показ истории ошибок и статусов' if not status_error else 'Выключить показ истории ошибок и статусов'}
        3. Показать всю историю
        4. Показать историю за дату
        5. Удалить историю вычислений
        6. Вернуться в главное меню""")
        value = input("Введите номер пункта меню: ")
        if not err.check_menu_error(value, menu_items):
            break
    return value


def get_date():
    """Показывает историю вычислений за дату"""
    while True:
        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        if not err.check_date_error(date):
            if err.check_date_exist_in_log(date):
                break
    return date
