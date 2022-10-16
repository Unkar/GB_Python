import logger as log
import datetime as dt


history_recording_status = True
history_error_visiable_status = True
history_status_visiable = True
PATH_LOG = 'log.txt'

def history_recording():
    global history_recording_status
    if history_recording_status == True:
        log.write_log_status("История выключена")
        print('История выключена')
    else:
        log.write_log_status('История включена')
        print('История включена')
    history_recording_status = not history_recording_status

def error_visiable():
    global history_error_visiable_status
    if history_error_visiable_status == True:
        history_error_visiable_status = False
        log.write_log_status("История ошибок выключена")
        print('История ошибок выключена')
    else:
        history_error_visiable_status = True
        log.write_log_status('История ошибок включена')
        print('История ошибок включена')