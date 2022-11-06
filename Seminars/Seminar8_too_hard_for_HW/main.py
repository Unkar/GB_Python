import errorhandling
import UI
import json_request
import shutil

def start():
    while True:
        choice = UI.start_window()
        if choice == "Вход":
            entrance()
        elif choice == "Выход":
            exit(0)
        elif choice == "О программе":
            UI.about_window()
        elif choice == "Помощь":
            UI.help_window()
        elif choice == "Справка":
            UI.reference_window()
        else:
            errorhandling.error_window("Ошибка в start_window")

def entrance():
    while True:
        log_pass= UI.entrance_window()
        if log_pass != None:
            #Проверка логина и пароля
            if json_request.check_login(log_pass[0], log_pass[1]):
                general(json_request.get_user_id(log_pass[0]))
            else:
                errorhandling.error_window("Неверный логин или пароль") 
        else:
            registration()

def registration():
    while True:
        log_pass = UI.registration_window()
        if log_pass != None:
            #Проверка логина и пароля
            if json_request.check_login(log_pass[0], log_pass[1]):
                errorhandling.error_window("Такой логин уже существует")
            else:
                #Регистрация
                general(json_request.registration(log_pass))

# 1. Трекер задач
# 2. Выбор объекта
# 3. Документация по объекту
# 3. Меню параметров объекта
def general(user_id:int, object_id:int = None):
    """object_id - id объекта, если None, то выбор объекта"""
    while True:
        choice = UI.general_window(user_id, object_id)
        if choice == 'Трекер задач':
            tracker(user_id, object_id)
        elif choice == 'Выбор объекта':
            object_id = choose_object(user_id)
        elif choice == "Документация по объекту":
            documentation(user_id, object_id)
        elif choice == "Меню параметров объекта":
            object_menu(user_id, object_id)
        elif choice == "Выход":
            break
        else:
            errorhandling.error_window("Ошибка в general_window")

def tracker(user_id:int, object_id:int):
    choice = json_request.get_documentation_id(UI.tracker_window(user_id, object_id))
    if choice != None:
        document_menu(user_id, object_id, choice)
    if choice == None:
        errorhandling.error_window("Документ не выбран")


def choose_object(user_id:int):
    """Возвращает id объекта"""
    choice = json_request.get_object_id(UI.choose_object_window(user_id))
    if choice == None:
        errorhandling.error_window("Объект не выбран")
    elif choice == "Добавить объект":
        add_object(user_id)
    else:
        return choice

def object_menu(user_id:int, object_id:int):
    while True:
        choice = UI.object_menu_window(user_id, object_id)
        if choice == "Изменить объект":
            change_object(user_id, object_id)
        elif choice == "Удалить объект":
            delete_object(user_id, object_id)
            break
        elif choice == "Выход":
            break
        else:
            errorhandling.error_window("Ошибка в object_menu_window")

def add_object(user_id:int):
    """Добавляет объект"""
    data = UI.add_object_window(user_id)
    if data != None:
        json_request.add_object(user_id, data)

def documentation(user_id:int, object_id:int):
    """Возвращает id документа из меню документации и запускает меню документа"""
    while True:
        choice = json_request.get_documentation_id(UI.documentation_window(user_id, object_id))
        if choice == "Добавить документ":
            add_documentation(user_id, object_id)
        if choice == None:
            break
        else:
            document_menu(user_id, object_id, choice)
    
def document_menu(user_id:int, object_id:int, document_id:int):
    choice = UI.document_menu_window(user_id, object_id, document_id)
    if choice == "Удалить документ":
        json_request.delete_document(user_id, object_id, document_id)
    elif choice == "Скачать документ":
        download_path = UI.download_file_window(user_id, object_id, document_id)
        shutil.copyfile(json_request.get_documentation_path(user_id, object_id, document_id), download_path)
    elif choice == "Запросить подпись":
        sign_request(user_id, object_id, document_id)

def add_documentation(user_id:int, object_id:int):
    file = UI.open_file()
    if file != None:
        new_path = json_request.add_documentation(user_id, object_id, file)
        shutil.copyfile(file, new_path)

def sign_request(user_id:int, object_id:int, document_id:int):
    document_title = json_request.get_documentation_title(user_id, object_id, document_id)
    supervisor_id = json_request.get_supervisor_id(UI.sign_request_window(user_id, object_id, document_title))
    if supervisor_id != None:
        json_request.add_sign(user_id, object_id, document_id, supervisor_id)
    else:
        errorhandling.error_window("Неверный id")

def main():
    start()

if __name__ == "__main__":
    main()