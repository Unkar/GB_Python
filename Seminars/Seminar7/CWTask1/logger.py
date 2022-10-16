import datetime as dt
import config as cfg



def write_log_calc(expression: str, result):
    """ Запись в лог вычислений """
    if cfg.history_recording_status:
        with open(cfg.PATH_LOG, 'a', encoding= 'utf-8') as f:
            f.write(f"""Date :: {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} ==>> Calc :: {expression}={result}\n""")

def write_log_error(error: str):
    """ Запись в лог ошибок """
    if cfg.history_recording_status:
        with open(cfg.PATH_LOG, 'a', encoding= 'utf-8') as f:
            f.write(f"""Date :: {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} ==>> Error :: {error}\n""")

def write_log_status(status: str):
    """ Запись в лог статуса """
    if  cfg.history_recording_status:
        with open(cfg.PATH_LOG, 'a', encoding= 'utf-8') as f:
            f.write(f"""Date :: {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} ==>> Status :: {status}\n""")

def read_all_log():
    """ Вывод всего лога как список словарей с ключами date, type, message """
    with open(cfg.PATH_LOG, 'r', encoding= 'utf-8') as f:
        log_list = []
        for line in f:
            log_element = {}
            log_element['date'] = line.split('::')[1].split('==>>')[0].strip()
            log_element['type'] = line.split('==>>')[1].split('::')[0].strip()
            log_element['message'] = line.split('==>>')[1].split('::')[1].strip()
            log_list.append(log_element)
    return log_list

def delete_history():
    """ Удаление лога """
    with open(cfg.PATH_LOG, 'w', encoding='utf-8') as f:
        f.write('')
    print('История удалена')
