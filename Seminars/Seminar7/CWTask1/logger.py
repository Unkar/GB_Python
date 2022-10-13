import datetime as dt

def write_log(expression, result):
    with open('calculations.txt', 'a') as f:
        f.write(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} : {expression} = {result}')

def read_log(option):
    if option:
        pass
    with open('calculations.txt', 'r') as f:
        return f.readlines()