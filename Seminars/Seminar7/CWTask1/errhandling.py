# Path: errhandling.py
import logger as log
import config as cfg
import datetime as dt

def check_menu_error(value: int, max_value: int):
    """Обрабатывает ошибку ввода пункта меню.
Если вводимые данные не соответствуют типу и значению данных, то выводит сообщение об ошибке и возвращает True."""
    menu_items = [str(i) for i in range(1,max_value+1)]
    if value  in menu_items:
        return False
    else:
        print("Ошибка ввода. Нет такого пункта в меню. Повторите ввод.")
        log.write_log_error("Ошибка ввода. Нет такого пункта в меню. Повторите ввод.")
        return True

def check_date_error(date: str):
    """Обрабатывает ошибку ввода даты.
Если вводимые данные не соответствуют типу и значению данных в формате '%d.%m.%Y', то выводит сообщение об ошибке и возвращает True."""
    try:
        dt.datetime.strptime(date, '%d.%m.%Y')
        return False
    except ValueError:
        print("Ошибка ввода. Неверный формат даты. Повторите ввод.")
        log.write_log_error("Ошибка ввода. Неверный формат даты. Повторите ввод.")
        return True

def check_date_exist_in_log(date: str):
    """Проверяет, есть ли введенная дата в логе.
Если дата есть в логе, то возвращает True."""
    log_list = log.read_all_log()
    for log_element in log_list:
        if log_element['date'].split()[0] == date:
            return True
    print(f"Нет записей в истории на {date}. Повторите ввод.")
    log.write_log_error(f"Нет записей в истории на {date}. Повторите ввод.") 
    return False
