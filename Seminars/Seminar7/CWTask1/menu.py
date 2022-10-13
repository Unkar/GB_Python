

from multiprocessing.sharedctypes import Value
from Seminars.Seminar7.CWTask1.errhandling import check_menu_error
from errhandling import check_menu_error

def main_menu():
    print(""""Главное меню:
    1. Запустить калькулятор
    2. Настройки калькулятора
    3. Выход""")
    value = input("Введите номер пункта меню: ")
    if check_menu_error(Value):
        main_menu()
    return value

def settings_menu():
    print(""""Настройки:
    1. Включить/выключить историю вычислений
    2. Показать всю историю вычислений
    3. Показать вычисления за дату
    4. Удалить историю вычислений
    5. Вернуться в главное меню""")
    value = input("Введите номер пункта меню: ")
    if check_menu_error(Value):
        settings_menu()
    return value

def main():
    main_menu()
