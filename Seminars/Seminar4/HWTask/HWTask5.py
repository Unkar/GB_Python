# задача 5 необязательная
#  Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа.
#  Тема чат-бота любая.
#  Просьба - постараться не использовать простой одномерный список.

# Я собственно и пошёл сюда обучаться, чтобы сделать программу, которая будет прикладная для меня.
# Так что я тут не совсем чат-бот написал, а просто программа, которая умеет работать с JSON файлом.
# Структура следующая - есть список объектов, у каждого объекта есть старший геодезист и его телефон,
# а также список ГРО, которые находятся на объекте. ГРО - это геодезическая разбивочная основа, точки с известными координатами.
# В общем моя тема) Надеюсь, что я правильно понял задание.

# export_marks.txt - это файл экспорта марок из базы данных
# import_marks.txt - это файл для импорта марок в базу данных
# Object_data.json - это файл с данными об объектах


import json


PATH = "Seminars/Seminar4/HWTask/"

def open_json():
    with open(PATH + "Object_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def save_json(data):
    with open(PATH + "Object_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False)

def add_object():
    try:
        data = open_json()
    except:
        data = []
    print("Добавление объекта")
    object_title = input("Введите название объекта: ")
    address = input("Введите адрес объекта: ")
    date = input("Введите дату начала строительства объекта: ")
    chief = input("Введите ФИО старшего геодезиста объекта: ")
    chief_phone = input("Введите телефон старшего геодезиста объекта: ")
    marks=[]
    object = {"Титул": object_title, "Адрес": address, "Дата": date, "Старший геодезист": chief, "Телефон": chief_phone, "ГРО": marks}
    data.append(object)
    save_json(data)
    print("Объект успешно добавлен!")

def list_objects():
    data = open_json()
    objects = []
    for i in data:
        objects.append(i["Титул"])
    return objects    

def print_objects():
    data = open_json()
    print("-----------------------")
    print("Список объектов:")
    for i in data:
        print(i["Титул"])
    print("-----------------------")

def list_contacts():
    data = open_json()
    contacts = []
    print("-----------------------")
    print("Контакты:")
    for i in data:
        print(i["Титул"], i["Старший геодезист"], i["Телефон"])
        contacts.append((i["Титул"], i["Старший геодезист"], i["Телефон"]))
    return contacts

def list_marks(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            for j in i["ГРО"]:
                print(j["Name"], j["X"], j["Y"], j["Z"], j["Code"])

def user_request(text_request):
    response = input(text_request+'(y/n): ')
    if response == 'y':
        return True
    else:
        return False    

def export_marks(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            file = PATH + "export_marks.txt"
            with open(file, "w", encoding="utf-8") as file:
                for j in i["ГРО"]:
                    file.write(j["Name"]+","+j["X"]+","+j["Y"]+","+j["Z"]+","+j["Code"])
    print("Файл успешно экспортирован!")
                    
         
def add_marks(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            while True:
                case = input("Добавить вручную (введите 1) или импортировать (введите 2) файл с координатами?(exit если отложить): ")
                if case == "1":
                    mark_name = input("Введите название точки: ")
                    mark_X = input("Введите координатe X(Cеверная): ")
                    mark_Y = input("Введите координатe Y(Восточная): ")
                    mark_Z = input("Введите координатe Z(Высота): ")
                    mark_code = input("Введите код точки: ")
                    mark = {"Name": mark_name, "X": mark_X, "Y": mark_Y, "Z": mark_Z, "Code": mark_code}
                    i["ГРО"].append(mark)
                    save_json(data)
                    print("Точка успешно добавлена!")
                elif case == "2":
                    file = input("Введите название файла: ")
                    file = PATH + file
                    with open(file, "r", encoding="utf-8") as file:
                        data_marks = [line.split(',') for line in file]
                        for j in data_marks:
                            mark = {"Name": j[0], "X": j[1], "Y": j[2], "Z": j[3], "Code": j[4] }
                            i["ГРО"].append(mark)
                    print("Файл успешно импортирован!")
                    save_json(data)
                elif case == "exit":
                    break
                else:
                    print("Неверная команда")

def delete_marks(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            while True:
                case = input("Удалить все марки (введите 1) или удалить марки по имени (введите 2)?(exit если отменить): ")
                if case == "1":
                    i["ГРО"] = []
                elif case == "2":
                    name = input("Введите имя марки: ")
                    for j in i["ГРО"]:
                        if j["Name"] == name:
                            i["ГРО"].remove(j)
                    print("Марки успешно удалены!")        
                elif case == "exit":
                    break
                else:
                    print("Неверная команда")
            save_json(data)

def change_chief(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            chief = input("Введите ФИО нового начальника объекта: ")
            chief_phone = input("Введите телефон нового начальника объекта: ")
            i["Старший геодезист"] = chief
            i["Телефон"] = chief_phone
            save_json(data)

def delete_object(object_title):
    data = open_json()
    for i in data:
        if i["Титул"] == object_title:
            data.remove(i)
            save_json(data)

def start_menu():
    while True:
        print("-----------------------")
        print("Главное меню:")
        print("1. Добавить объект")
        print("2. Удалить объект")
        print("3. Список объектов")
        print("4. Контакты")
        print("5. Войти в меню объекта")
        print("6. Выход")
        case = input("Введите номер пункта меню: ")
        print("-----------------------")
        if case == "1":
            add_object()
        elif case == "2":
            object_title = input("Введите название объекта: ")
            delete_object(object_title)
        elif case == "3":
            print_objects()
        elif case == "4":
            list_contacts()
        elif case == "5":
            print_objects()
            object_title = input("Введите название объекта: ")
            object_menu(object_title)
        elif case == "6":
            break
        else:
            print("Неверная команда")

def object_menu(object_title):
    while object_title in list_objects():
        print("-----------------------")
        print("Меню объекта: " + object_title)
        print("1. Добавить координаты марок")
        print("2. Удалить марки")
        print("3. Список координат марок")
        print("4. Изменить начальника объекта")
        print("5. Выгрузить марки в файл")
        print("6. Выход")
        case = input("Введите номер пункта меню: ")
        print("-----------------------")
        if case == "1":
            add_marks(object_title)
        elif case == "2":
            delete_marks(object_title)
        elif case == "3":
            list_marks(object_title)
        elif case == "4":
            change_chief(object_title)
        elif case == "5":
            export_marks(object_title)
        elif case == "6":
            break
        else:
            print("Неверная команда")

def main():
    print("Программа для работы с базой данных ГРО")
    start_menu()

if __name__ == "__main__":
    main()
