import errhandling as err
import config as cfg
import logger as log


def main_menu():
    """Основное меню калькулятора"""
    menu_items = 4
    while True:
        print(""""Главное меню:
        1. Запустить калькулятор выражений
        2. Запустить калькулятор комплексных чисел
        3. Настройки калькулятора
        4. Выход""")
        value = input("Введите номер пункта меню: ")
        if not err.check_menu_error(value, menu_items):
            break
    return value


def settings_menu():
    """Меню настроек"""
    status = cfg.history_recording_status
    status_error = cfg.history_error_visiable_status
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

def print_all_history(history_error_visiable_status: bool):
    """Показывает всю историю вычислений"""
    log_list = log.read_all_log()
    if history_error_visiable_status:
        for log_element in log_list:
            print(
                f"{log_element['date']} :: {log_element['type']} :: {log_element['message']}")
    else:
        for log_element in log_list:
            if log_element['type'] != 'Error' and log_element['type'] != 'Status':
                print(
                    f"{log_element['date']} :: {log_element['type']} :: {log_element['message']}")
    log.write_log_status("Просмотр истории")


def print_history_by_date(date: str, history_error_visiable_status: bool):
    """Показывает историю вычислений за дату"""
    log_list = log.read_all_log()
    if history_error_visiable_status:
        for log_element in log_list:
            if log_element['date'].split()[0] == date:
                print(
                    f"{log_element['date']} :: {log_element['type']} :: {log_element['message']}")
    else:
        for log_element in log_list:
            if log_element['date'].split()[0] == date and log_element['type'] != 'Error' and log_element['type'] != 'Status':
                print(
                    f"{log_element['date']} :: {log_element['type']} :: {log_element['message']}")
    log.write_log_status(f"Просмотр истории за {date}")