PATH = "Seminars/Seminar5/HWTask/"

def random_string_generator(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def save_string_to_file(filename, string):
    with open(filename, 'w') as f:
        f.write(string)

def main():
    string_length = int(input('Введите длину строки: '))
    filename = PATH + "HWT_input_string.txt"
    save_string_to_file(filename, random_string_generator(string_length))

if __name__ == '__main__':
    main()