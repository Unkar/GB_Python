import random
import string

PATH = "Seminars/Seminar5/HWTask/"

def random_string_generator(quantity_generation):
    return ''.join(random.choice(string.ascii_letters)*random.randint(1,4) for i in range(quantity_generation))

def save_string_to_file(filename, string):
    with open(filename, 'w') as f:
        f.write(string)

def main():
    # Коэффициент генерации строк, сколько раз будет генерироваться символы в строке.
    # Сделан, чтобы были совпадающие символы в строке.
    quantity_generation = int(input('Введите коэффициент генерациии: '))
    filename = PATH + "HWT_input_string.txt"
    save_string_to_file(filename, random_string_generator(quantity_generation))

if __name__ == '__main__':
    main()