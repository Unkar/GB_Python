import re
import logger as log


def convert_complex_to_tupal(complex_number: str):
    complex_number = complex_number.replace(' ', '')
    complex_number = complex_number.replace('+-', '-')
    complex_number = complex_number.replace('--', '+')
    complex_number = complex_number.replace('++', '+')
    complex_number = complex_number.replace('-+', '-')
    complex_pattern = re.compile(
        r'(?P<real_part>-?\d+)?(?P<imaginary_part>[+-]?\d*i)?')
    complex_match = complex_pattern.match(complex_number)
    if complex_match:
        real_part = complex_match.group('real_part')
        print(real_part)
        print(type(real_part))
        imaginary_part = complex_match.group('imaginary_part')
        print(imaginary_part)
        print(type(imaginary_part))
        if real_part == None:
            real_part = 0
        else:
            real_part = float(real_part)
        if imaginary_part != '':
            if imaginary_part == '+i' or "i":
                imaginary_part = 1
            elif imaginary_part == '-i':
                imaginary_part = -1
            else:
                imaginary_part = float(imaginary_part.replace('i', ''))
        else:
            imaginary_part = 0
        return (real_part, imaginary_part)
    else:
        return None


def convert_tupal_to_complex(complex_number: tuple):
    """Конвертация кортежа в комплексное число"""
    if complex_number[0] == 0:
        return f'{complex_number[1]}i'
    elif complex_number[1] == 0:
        return f'{complex_number[0]}'
    elif complex_number[1] > 0:
        return f'{complex_number[0]}+{complex_number[1]}i'
    else:
        return f'{complex_number[0]}{complex_number[1]}i'


def sum_complex(number_1: str, number_2: str):
    """Сложение комплексных чисел"""
    complex_number_1 = convert_complex_to_tupal(number_1)
    complex_number_2 = convert_complex_to_tupal(number_2)
    return convert_tupal_to_complex((complex_number_1[0] + complex_number_2[0], complex_number_1[1] + complex_number_2[1]))


def sub_complex(number_1: str, number_2: str):
    """Вычитание комплексных чисел"""
    complex_number_1 = convert_complex_to_tupal(number_1)
    complex_number_2 = convert_complex_to_tupal(number_2)
    return convert_tupal_to_complex((complex_number_1[0] - complex_number_2[0], complex_number_1[1] - complex_number_2[1]))


def multiply_complex(complex_number_1: str, complex_number_2: str):
    """Умножение комплексных чисел"""
    return convert_tupal_to_complex(((complex_number_1[0] * complex_number_2[0] - complex_number_1[1] * complex_number_2[1]), (complex_number_1[0] * complex_number_2[1] + complex_number_1[1] * complex_number_2[0])))


def divide_complex(complex_number_1: str, complex_number_2: str):
    """Деление комплексных чисел"""
    return convert_tupal_to_complex(((complex_number_1[0] * complex_number_2[0] + complex_number_1[1] * complex_number_2[1]) / (complex_number_2[0] ** 2 + complex_number_2[1] ** 2), (complex_number_1[1] * complex_number_2[0] - complex_number_1[0] * complex_number_2[1]) / (complex_number_2[0] ** 2 + complex_number_2[1] ** 2)))


def main():
    while True:
        if input("для выхода нажмите 'q' или 'Q', для продолжения нажмите Enter") in ('q', 'Q'):
            break
        try:
            complex_number_1 = input("Введите первое комплексное число: ")
            complex_number_2 = input("Введите второе комплексное число: ")
            op = input('Введите операцию: ')
            if op == '+':
                return sum_complex(complex_number_1, complex_number_2)
            elif op == '-':
                return sub_complex(complex_number_1, complex_number_2)
            elif op == '*':
                return multiply_complex(complex_number_1, complex_number_2)
            elif op == '/':
                return divide_complex(complex_number_1, complex_number_2)
            elif op == 'q' or op == 'Q':
                break
            else:
                print('Неверная операция. Попробуйте еще раз.')
        except Exception as e:
            print("Ошибка ввода выражения. Повторите ввод. Тип ошибки:" + str(e))
            log.write_log_error(
                "Ошибка ввода выражения. Повторите ввод. Тип ошибки: " + str(e))


if __name__ == '__main__':
    main()
