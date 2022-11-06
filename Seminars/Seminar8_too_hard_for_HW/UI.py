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
    choice = easygui.buttonbox(msg, title, choices)
    return  choice

# Окно входа
def entrance_window():
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
    choices.append("Добавить объект")
    choice = easygui.choicebox(msg, title, choices)
    return choice

def object_menu_window(user_id:str, object_id:str):
    """Окно меню объекта"""
    msg = "Выберите действие"
    title = f"Пользователь:{user_id}. Объект:{object_id}"
    choices = ["Изменить объект", "Удалить объект", "Выход"]
    choice = easygui.choicebox(msg, title, choices)
    return choice

def add_object_window(user_id:str, object_id:str = None):
    """Окно добавления объекта"""
    if object_id:
        msg = "Введите данные для изменения объекта"
        title = f"Изменение объекта. Пользователь:{user_id}. Объект:{object_id}"
    else:
        msg = "Введите данные для добавления объекта"
        title = f"Добавить объект. Пользователь:{user_id}"
        field_names = ["Название объекта", "Адрес объекта", "Дата начала работ"]
    field_values = easygui.multenterbox(msg, title, field_names)
    data = {
        'object_title': field_values[0],
        'object_address': field_values[2],
        'object_start_date': field_values[3]
    }
    return data

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
    title = "Загрузить документ из базы"
    download_path = easygui.filesavebox(msg, title)
    return download_path

def open_file_window(user_id:str, object_id:str, file_path:str):
    """Окно открытия файла"""
    msg = "Выберите действие"
    title = "Закгрузить документ в базу"
    download_path = easygui.filesavebox(msg, title)
    return download_path

def sign_request_window(user_id:str, object_id:str, document_title:str):
    """Окно запроса подписи"""
    msg = "Выберите сотрудника для запроса подписи"
    title = f"Запросить подпись. Пользователь:{user_id}. Объект:{object_id}. Документ:{document_title}"
    choices = json_request.get_employee_list(user_id, object_id)
    choice = easygui.choicebox(msg, title, choices)
    return choice

def about_window():
    """Окно о программе"""
    msg = "О программе"
    title = "О программе"
    easygui.msgbox(msg, title)

def help_window():
    """Окно справки"""
    msg = "Помощь"
    title = "Помощь"
    easygui.msgbox(msg, title)

def reference_window():
    """Окно справки"""
    msg = "Справка"
    title = "Справка"
    easygui.msgbox(msg, title)

