""" На функцию подаётся выражение в текстовом виде. Необходимо вернуть результат вычисления. """
import logger as log

def calculate_rational(expression: str):
    """ Вычисление рациональных выражении без скобок """
    if expression.find('+') != -1:
        return calculate_rational(expression[:expression.find('+')]) + calculate_rational(expression[expression.find('+')+1:])
    elif expression.find('-') != -1:
        return calculate_rational(expression[:expression.find('-')]) - calculate_rational(expression[expression.find('-')+1:])
    elif expression.find('*') != -1:
        return calculate_rational(expression[:expression.find('*')]) * calculate_rational(expression[expression.find('*')+1:])
    elif expression.find('/') != -1:
        return calculate_rational(expression[:expression.find('/')]) / calculate_rational(expression[expression.find('/')+1:])
    else:
        return float(expression)

def calculate(expression: str):
    """ Вычисление выражении с учётом скобок """
    while expression.find(')') != -1:
        expression = expression[:expression.rfind('(', 0, expression.find(')'))] + str(calculate_rational(expression[expression.rfind('(', 0, expression.find(')'))+1:expression.find(')')])) + expression[expression.find(')')+1:]
    return calculate_rational(expression)

def main():
    """ Основная функция """
    while True:
        expression = input("Введите выражение (для выхода введите 'q'): ")
        try:
            if expression == 'q':
                break
            print(expression + ' = ' + str(calculate(expression)))
            log.write_log_calc(expression, calculate(expression))
        except Exception as e:
            print("Ошибка ввода выражения. Повторите ввод. Тип ошибки:" + str(e))
            log.write_log_error("Ошибка ввода выражения. Повторите ввод. Тип ошибки:" + str(e))


if __name__ == '__main__':
    main()