import config as cfg
import errhandling as err
import menu as m
import logger as log
import datetime as dt
import calculator as calc
import complex_calculator as cc


def main():
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
    while True:
        value = m.settings_menu()
        if value == '1':
            cfg.history_recording()
        elif value == '2':
            cfg.error_visiable()
        elif value == '3':
            print_all_history(cfg.history_error_visiable_status)
        elif value == '4':
            print_history_by_date(
                m.get_date(), cfg.history_error_visiable_status)
        elif value == '5':
            delete_history()
        elif value == '6':
            break


def print_all_history(history_error_visiable_status):
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


def print_history_by_date(date, history_error_visiable_status):
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


def delete_history():
    with open(cfg.PATH_LOG, 'w', encoding='utf-8') as f:
        f.write('')
    print('История удалена')


if __name__ == '__main__':
    main()
