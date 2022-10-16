import config as cfg
import errhandling as err
import menu as m
import logger as log
import datetime as dt
import calculator as calc
import complex_calculator as cc


def main():
    """Основная функция программы."""
    while True:
        value = m.main_menu()
        if value == '1':
            calc.main()
        elif value == '2':
            cc.main()
        elif value == '3':
            settings_menu()
        elif value == '4':
            break


def settings_menu():
    """Функция меню настроек."""    
    while True:
        value = m.settings_menu()
        if value == '1':
            cfg.history_recording()
        elif value == '2':
            cfg.error_visiable()
        elif value == '3':
            m.print_all_history(cfg.history_error_visiable_status)
        elif value == '4':
            m.print_history_by_date(
                m.get_date(), cfg.history_error_visiable_status)
        elif value == '5':
            log.delete_history()
        elif value == '6':
            break

if __name__ == '__main__':
    main()
