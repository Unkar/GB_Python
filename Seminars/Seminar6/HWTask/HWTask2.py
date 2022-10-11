# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

def calculate(expression):
    if expression.find('+') != -1:
        return calculate(expression[:expression.find('+')]) + calculate(expression[expression.find('+')+1:])
    elif expression.find('-') != -1:
        return calculate(expression[:expression.find('-')]) - calculate(expression[expression.find('-')+1:])
    elif expression.find('*') != -1:
        return calculate(expression[:expression.find('*')]) * calculate(expression[expression.find('*')+1:])
    elif expression.find('/') != -1:
        return calculate(expression[:expression.find('/')]) / calculate(expression[expression.find('/')+1:])
    else:
        return float(expression)

def calculate_with_brackets(expression):
    while expression.find(')') != -1:
        expression = expression[:expression.rfind('(', 0, expression.find(')'))] + str(calculate(expression[expression.rfind('(', 0, expression.find(')'))+1:expression.find(')')])) + expression[expression.find(')')+1:]
    return calculate(expression)

def main():
    print(calculate_with_brackets(input('Введите выражение: ')))

if __name__ == '__main__':
    main()
