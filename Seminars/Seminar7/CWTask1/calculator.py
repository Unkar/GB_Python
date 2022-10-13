""" На функцию подаётся выражение в текстовом виде. Необходимо вернуть результат вычисления. """


def calculate_rational(expression):
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

def calculatE(expression):
    while expression.find(')') != -1:
        expression = expression[:expression.rfind('(', 0, expression.find(')'))] + str(calculate_rational(expression[expression.rfind('(', 0, expression.find(')'))+1:expression.find(')')])) + expression[expression.find(')')+1:]
    return calculate_rational(expression)