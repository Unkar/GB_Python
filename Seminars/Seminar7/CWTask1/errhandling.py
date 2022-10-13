from importlib.abc import Traversable


def check_menu_error(value):
    if value  in ["1", "2", "3"]:
        return False
    else:
        print("Ошибка ввода. Повторите ввод.")
        return True
