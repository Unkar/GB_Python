#db.json structure
#db = [{'user_id': 'user_id1',
#       'user_login': 'user_login',
#       'user_password': 'user_password',
#       'user_surname': 'user_surname',
#       'user_name': 'user_name',
#       'user_patronymic': 'user_patronymic',
#       'user_birthday': 'user_birthday',
#       'user_phone': 'user_phone',
#       'user_email': 'user_email'
#       'about_me': 'about_me',
#       'user_status': 'user_status'},
#      {'user_id': 'user_id2', ...}]

#viewed.json structure
#viewed_list = [{'viewer': 'user_id1', 'viewed': 'user_id2', date: 'date'},...]
import json
import os
import config
import datetime


def get_db():
    with open(config.PATH_DB, 'r', encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open(config.PATH_DB, 'w', encoding="utf-8") as f:
        json.dump(db, f)


def get_user_id(user_login):
    db = get_db()
    for user in db:
        if user['user_login'] == user_login:
            return user['user_id']

def check_login(user_login, user_password = None):
    db = get_db()
    if db is None:
        return False
    if user_password == None:
        for user in db:
            if user['user_login'] == user_login:
                return True
        return False
    else:
        for user in db:
            if user['user_login'] == user_login and user['user_password'] == user_password:
                return True
        return False

def registration(user_info):
    db = get_db()
    user_id = f"UID:{str(len(db) + 1)}"
    db.append({'user_id': user_id,
               'user_login': user_info[0],
               'user_password': user_info[1],
               'user_surname': user_info[3],
               'user_name': user_info[4],
               'user_patronymic': user_info[5],
               'user_birthday': user_info[6],
               'user_phone': user_info[7],
               'user_email': user_info[8],
               'about_me': user_info[9],
               'user_status': user_info[10]})
    save_db(db)
    return user_id

def get_user_info(user_id):
    db = get_db()
    for user in db:
        if user['user_id'] == user_id:
            return user

def get_user_status(user_id):
    db = get_db()
    for user in db:
        if user['user_id'] == user_id:
            return user['user_status']

def get_users():
    db = get_db()
    users = []
    for user in db:
        users.append(f"{user['user_id']} ::: {user['user_surname']} {user['user_name']} {user['user_birthday']} {user['user_status']}")
    return users

def get_users_by_status(user_status):
    db = get_db()
    users = []
    for user in db:
        if user['user_status'] == user_status:
            users.append(f"{user['user_id']} ::: {user['user_surname']} {user['user_name']} {user['user_birthday']} {user['user_status']}")
    return users

def get_viewed_list(user_id):
    viewed_list = []
    personal_viewed_list = []
    with open(config.PATH_VIEWED, 'r', encoding="utf-8") as f:
        viewed_list = json.load(f)
    for viewed in viewed_list:
        if viewed['viewer'] == user_id:
            personal_viewed_list.append(f"{viewed['viewed']} ::: {viewed['date']}")
    return personal_viewed_list

def get_viewer_list(user_id):
    viewed_list = []
    personal_viewer_list = []
    db = get_db()
    with open(config.PATH_VIEWED, 'r', encoding="utf-8") as f:
        viewed_list = json.load(f)
    for viewed in viewed_list:
        if viewed['viewed'] == user_id:
            for user in db:
                if user['user_id'] == viewed['viewer']:
                    personal_viewer_list.append(f"{user['user_id']} ::: {user['user_surname']} {user['user_name']} {user['user_birthday']} {user['user_status']} ::: {viewed['date']}")
            personal_viewer_list.append(f"{viewed['viewer']} :::  {viewed['date']}")
    return personal_viewer_list

def add_viewed(viewer, viewed):
    viewed_list = []
    with open(config.PATH_VIEWED, 'r', encoding="utf-8") as f:
        viewed_list = json.load(f)
    viewed_list.append({'viewer': viewer, 'viewed': viewed, 'date': f"{datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"})
    with open(config.PATH_VIEWED, 'w', encoding="utf-8") as f:
        json.dump(viewed_list, f)

   