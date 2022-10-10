# 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;


def calc(expression):
    if expression.find('+') != -1:
        return calc(expression[:expression.find('+')]) + calc(expression[expression.find('+') + 1:])
    if expression.find('-') != -1:
        return calc(expression[:expression.find('-')]) - calc(expression[expression.find('-') + 1:])
    if expression.find('*') != -1:
        return calc(expression[:expression.find('*')]) * calc(expression[expression.find('*') + 1:])
    if expression.find('/') != -1:
        return calc(expression[:expression.find('/')]) / calc(expression[expression.find('/') + 1:])
    return float(expression)

print(calc(input()))
