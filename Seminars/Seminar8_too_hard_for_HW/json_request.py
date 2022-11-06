#База данных объетков
#objects = [{'main_base': [{'object_id': 1,
#                            'object_info':{
#                                            'object_title': 'title1',
#                                            'object_adress': 'adress',
#                                            'object_start_date': 'start_date'
#                                          },
#                            'object_documents':[{'document_id': 'document_id1',
#                                                'document_title': 'document_title',
#                                                'document_date': 'document_date',
#                                                'document_author': 'document_author',
#                                                'document_path': 'document_path',
#                                                'document_type': 'document_type',
#                                                'document_description': 'document_description',
#                                                'document_for_whom': 'user_id',
#                                                'document_sign': ['user_id', 'user_id'],
#                                                'object_document_status': 'document_status'},
#                                                {'document_id': 'document_id2', ...},],
#                           {'object_id': 2, ...}],
#            'users_base': [{'user_id': 'user_id1',
#                            'user_info': {'user_name': 'user_name',
#                                          'user_surname': 'user_surname',
#                                          'user_patronymic': 'user_patronymic',
#                                          'user_position': 'user_position',
#                                          'user_birthday': 'user_birthday',
#                                          'user_phone': 'user_phone',
#                                          'user_email': 'user_email'}
#                            'user_login': 'user_login',
#                            'user_password': 'user_password',
#                            'user_role': 'user_role',
#                            'user_status': 'user_status'},
#                            {'user_id': 'user_id2', ...}],
import json
import os
import config
import logger

PATH = config.JSON_PATH


def get_json(path):
    """Получение json"""
    with open(path, 'r') as f:
        objects = json.load(f)
    return objects

def save_json(objects, path = PATH):
    """Сохранение json"""
    with open(path, 'w') as f:
        json.dump(objects, f)

objects = get_json(PATH)

def check_login(login:str, password:str):
    """Проверка логина и пароля"""
    global objects
    for user in objects['users_base']:
        if user['user_login'] == login and user['user_password'] == password:
            logger.addlog('Cистема', user['user_id'], 'Вход в систему', 'Успешно')
            return user['user_id']
    logger.addlog('Cистема', 'Неизвестный пользователь', 'Вход в систему', 'Неуспешно')

def get_user_id(user_id):
    """Получение информации о пользователе"""
    global objects
    for user in objects['users_base']:
        if user['user_id'] == user_id:
            return user
            
def get_documents_for_sign(user_id, object_id):
    """Получение документов для подписи"""
    global objects
    documents = []
    for document in objects['main_base'][object_id]['object_documents']:
        if user_id in document['document_for_whom'] and user_id not in document['document_sign']:
            documents.append(document)
    return documents

def get_object_list(user_id):
    """Получение списка объектов"""
    global objects
    object_list = []
    for object in objects['main_base']:
        if user_id in object['object_documents'][0]['document_for_whom']:
            object_list.append(object)
    return object_list   

def get_documentation_list(user_id, object_id):
    """Получение списка документации"""
    global objects
    documentation_list = []
    for document in objects['main_base'][object_id]['object_documents']:
        if user_id in document['document_for_whom']:
            documentation_list.append(document)
    return documentation_list