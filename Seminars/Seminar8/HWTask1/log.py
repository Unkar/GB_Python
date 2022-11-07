#log.json - файл лога
#log.py - модуль для работы с логом
#
#log.json = [ { "date": "2019-11-11 11:11:11", "type": "type1", "user": "user1", "module": "module1", "param": "param1" },
#              { "date": "2019-11-11 11:11:11", "type": "type2", "user": "user1", "module": "module1", "param": "param1" },
#              { "date": "2019-11-11 11:11:11", "type": "type3", "user": "user1", "module": "module1", "param": "param1" }
#            ]

import json
import datetime
import easygui as eg
import config


def get_log():
    with open(config.PATH_LOG, "r", encoding="utf-8") as log:
        return json.load(log)

def save_log(log_message):
    with open(config.PATH_LOG, "w", encoding="utf-8") as log:
        json.dump(log_message, log, ensure_ascii=False)

def add_log(type:str, user:str, module:str, param:str):
    log = get_log()
    log.append({"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "type": type, "user": user, "module": module, "param": param})
    save_log(log)

def show_log():
    log = get_log()
    msg = ""
    for i in log:
        msg += f"{i['date']} {i['type']} {i['user']} {i['module']} {i['param']} \n"
    eg.textbox(msg=msg, title="Log")

def add_viewed(user:str, viewed:str):
    add_log("viewed", user, "main", viewed)

def main():
    show_log()

if __name__ == "__main__":
    main()

