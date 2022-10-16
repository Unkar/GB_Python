import logger as log



history_recording_status = True # Включение и выключение записи истории
history_error_visiable_status = True    # Включение и выключение отображения ошибок
history_status_visiable = True 
PATH_LOG = 'log.txt' # Путь к файлу с историей

def history_recording():
    """Включение и выключение записи истории"""
    global history_recording_status
    if history_recording_status == True:
        log.write_log_status("История выключена")
        print('История выключена')
    else:
        log.write_log_status('История включена')
        print('История включена')
    history_recording_status = not history_recording_status

def error_visiable():
    """Включение и выключение отображения ошибок"""
    global history_error_visiable_status
    if history_error_visiable_status == True:
        history_error_visiable_status = False
        log.write_log_status("История ошибок выключена")
        print('История ошибок выключена')
    else:
        history_error_visiable_status = True
        log.write_log_status('История ошибок включена')
        print('История ошибок включена')