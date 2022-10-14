import errhandling as err
import config


def main_menu():
    """Основное меню калькулятора"""
    menu_items = 3
    print(""""Главное меню:
    1. Запустить калькулятор
    2. Настройки калькулятора
    3. Выход""")
    value = input("Введите номер пункта меню: ")
    if err.check_menu_error(value,3):
        main_menu()
    return value


def settings_menu():
    """Меню настроек"""
    menu_items = 5
    print(""""Настройки:
    1. Включить/выключить историю вычислений
    2. Показать всю историю вычислений
    3. Показать вычисления за дату
    4. Удалить историю вычислений
    5. Вернуться в главное меню""")
    value = input("Введите номер пункта меню: ")
    if err.check_menu_error(value,menu_items):
        settings_menu()
    return value

def history_visiable():
    """Включает/выключает историю вычислений"""
    menu_items = 2
    status = config.history_visiable_status
    print(f""""История вычислений:
    Статуст: {'включена' if status else 'выключена'}
    1. {'Включить' if status else 'Выключить'}
    2. Выход""")
    value = input("Введите номер пункта меню: ")
    if err.check_menu_error(value,menu_items):
        history_visiable()
    return value

def print_history():
    """Показывает историю вычислений"""
    pass

def print_history_by_date():
    """Показывает историю вычислений за дату"""
    pass

def delete_history():
    """Удаляет историю вычислений"""
    pass