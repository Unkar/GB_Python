# Path: errhandling.py
def check_menu_error(value, max_value):
    """Обрабатывает ошибку ввода пункта меню.
Если вводимые данные не соответствуют типу и значению данных, то выводит сообщение об ошибке и возвращает True."""
    menu_items = [str(i) for i in range(1,max_value+1)]
    if value  in menu_items:
        return False
    else:
        print("Ошибка ввода. Нет такого пункта в меню. Повторите ввод.")
        return True

