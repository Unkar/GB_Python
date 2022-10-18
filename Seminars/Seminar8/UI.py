import shutil
import easygui
import errorhandling
import json_request

# Стартовое окно программы

def start_window():
    """Стартовое окно программы"""
    msg = "Выберите действие"
    title = "Главное меню"
    choices = ["Вход", "Выход", "О программе", "Помощь", "Справка"]
    choice = easygui.choicebox(msg, title, choices)
    return  choice

# Окно входа
def entance_window():
    """Окно входа"""
    msg = "Введите логин и пароль"
    title = "Вход"
    fieldNames = ["Логин", "Пароль"]
    fieldValues = ['Для регистрации нажмите ОК без заполнения полей']  
    fieldValues = easygui.multpasswordbox(msg, title, fieldNames)
    return fieldValues

# Окно регистрации
def registration_window():
    """Окно регистрации"""
    msg = "Введите данные для регистрации"
    title = "Регистрация"
    fieldNames = ["Логин", "Пароль", "Повтор пароля", "Имя", "Фамилия", "Отчество", "Дата рождения", "Номер телефона", "Адрес электронной почты"]
    fieldValues = ['login1', 'password1', 'password1', 'Иван', 'Иванов', 'Иванович', '01.01.2000', '8-800-555-35-35', 'mail@mail.ma']
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    return fieldValues

# Главное окно программы
# 1. Трекер задач
# 2. Выбор объекта
# 3. Документация по объекту
# 3. Меню параметров объекта
def general_window(login:str, object_name:str = None):
    """Главное окно программы"""
    msg = "Выберите действие"
    title = f"Главное меню. Пользователь:{login}"
    if object_name:
        title = f"Главное меню. Пользователь:{login}. Объект:{object_name}"
    choices = ["Трекер задач", "Выбор объекта", "Документация по объекту", "Меню параметров объекта", "Выход"]
    if object_name == None:
        choices = ["Выбрать объект", "Выход"]   
    choice = easygui.choicebox(msg, title, choices)
    return choice

def tracker_window(user_id:str, object_id:str):
    """Окно трекера задач"""
    msg = "Список документов на подписание"
    title = f"Трекер задач. Пользователь:{user_id}. Объект:{object_id}"
    choices = json_request.get_documents_for_sign(user_id, object_id)
    choice = easygui.choicebox(msg, title, choices)
    return choice


# Окно выбора объекта
def choose_object_window(user_id:str):
    """Окно выбора объекта"""
    msg = "Выберите объект"
    title = f"Выбор объекта. Пользователь:{user_id}"
    choices = json_request.get_object_list()
    choice = easygui.choicebox(msg, title, choices)
    return choice

def documentation_window(user_id:str, object_id:str):
    """Окно списка документации по объекту"""
    msg = "Документация по объекту"
    title = f"Документация по объекту. Пользователь:{user_id}. Объект:{object_id}"  
    choices = json_request.get_documentation_list(user_id, object_id)
    choiсes.append("Добавить документ")
    choice = easygui.choicebox(msg, title, choices)
    return choice

def document_menu_window(User_id:str, object_id:str, documentation_id:str):
    """Окно меню документа"""
    msg = "Выберите действие"
    title = f"Пользователь:{User_id}. Объект:{object_id}. Документация:{documentation_id}"
    choices = ["Скачать документ", "Удалить документ", "Запросить подпись", "Выход"]
    choice = easygui.choicebox(msg, title, choices)
    return choice

def download_file_window(user_id:str, object_id:str, document_id:str):
    """Окно сохранения файла"""
    msg = "Выберите действие"
    title = "Скачать документ"
    download_path = easygui.filesavebox(msg, title)
    return download_path

def open_file_window(user_id:str, object_id:str, file_path:str):
    """Окно открытия файла"""
    msg = "Выберите действие"
    title = "Открыть документ"
    download_path = easygui.filesavebox(msg, title)
    return download_path

def sign_request_window(user_id:str, object_id:str, document_title:str):
    """Окно запроса подписи"""
    msg = "Выберите сотрудника для запроса подписи"
    title = f"Запросить подпись. Пользователь:{user_id}. Объект:{object_id}. Документ:{document_title}"
    choices = json_request.get_employee_list(user_id, object_id)
    choice = easygui.choicebox(msg, title, choices)

