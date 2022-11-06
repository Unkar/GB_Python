#log.json - файл лога
#logger.py - модуль для работы с логом
#
#log.json = [ { "date": "2019-11-11 11:11:11", "type": "type1", "user": "user1", "module": "module1", "param": "param1" },
#              { "date": "2019-11-11 11:11:11", "type": "type2", "user": "user1", "module": "module1", "param": "param1" },
#              { "date": "2019-11-11 11:11:11", "type": "type3", "user": "user1", "module": "module1", "param": "param1" }
#            ]

import json
import datetime
import easygui as eg


def get_log():
    with open("log.json", "r") as log:
        return json.load(log)

def save_log(log):
    with open("log.json", "w") as log:
        json.dump(log, log)

def add_log(type:str, user:str, module:str, param:str):
    log = get_log()
    log.append({"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "type": type, "user": user, "module": module, "param": param})
    save_log(log)

def get_log_by_type(type:str):
    log = get_log()
    return [i for i in log if i["type"] == type]

def get_log_by_user(user:str):
    log = get_log()
    return [i for i in log if i["user"] == user]

def get_log_by_module(module:str):
    log = get_log()
    return [i for i in log if i["module"] == module]

def get_log_by_param(param:str):
    log = get_log()
    return [i for i in log if i["param"] == param]

def get_log_by_date(date:str):
    log = get_log()
    return [i for i in log if i["date"] == date]

def get_log_by_date_range(date1:str, date2:str):
    log = get_log()
    return [i for i in log if i["date"] >= date1 and i["date"] <= date2]

def main():
    log = get_log()
    eg.msgbox(msg = log, title = "Log")

if __name__ == "__main__":
    main()

