# задача 2. Реализуйте RLE алгоритм: реализуйте модуль
#  сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

import HWT2_String_generator as hwt2


PATH_ORIGINAL_STRING = "Seminars/Seminar5/HWTask/HWT2_original_string.txt"
PATH_RLE_STRING = "Seminars/Seminar5/HWTask/HWT2_RLE_string.txt"
PATH_DECOMPRESSED_STRING = "Seminars/Seminar5/HWTask/HWT2_decompressed_string.txt"
TOP_DIVIDER = "-"*50+"\n"
BOTTOM_DIVIDER = "\n"+"-"*50


def get_rle_list_from_orig_string(original_string):
    rle_list = []
    count = 1
    for i in range(len(original_string)):
        if i == len(original_string) - 1:
            rle_list.append((count, original_string[i]))
        elif original_string[i] == original_string[i + 1]:
            count += 1
        else:
            rle_list.append((count, original_string[i]))
            count = 1
    return rle_list

def get_rle_string_from_rle_list(RLE_list):
    rle_sting = ""
    for i in RLE_list:
        rle_sting += str(i[0]) + i[1]
    return rle_sting


def get_rle_list_from_rle_string(rle_string):
    rle_list = []
    while len(rle_string) > 0:
        for i in rle_string:
            if not i.isdigit():
                rle_list.append((int(rle_string[:rle_string.index(i)]), i))
                rle_string = rle_string[rle_string.index(i) + 1:]
                break
    return rle_list


def get_orig_string_from_rle_list(RLE_list):
    orig_string = ""
    for i in RLE_list:
        orig_string += i[1] * i[0]
    return orig_string


def save_string_to_file(filename, string):
    with open(filename, 'w') as f:
        f.write(string)


def compressions_ratio():
    with open(PATH_ORIGINAL_STRING, 'r') as f:
        orig_string = f.read()
    with open(PATH_RLE_STRING, 'r') as f:
        rle_string = f.read()
    with open(PATH_DECOMPRESSED_STRING, 'r') as f:
        decompressed_string = f.read()
    check_right_decompression = orig_string == decompressed_string
    print(f"""{TOP_DIVIDER}ОТЧЕТ ПО СЖАТИЮ
Оригинальная строка: {orig_string}
Длина оригинальной строки: {len(orig_string)} символов.
Сжатая строка: {rle_string}
Длина сжатой строки: {len(rle_string)} символов.
Восстановленная строка: {decompressed_string}
Длина восстановленной строки: {len(decompressed_string)} символов.
Строки оригинальная и восстановленная совпадают: {check_right_decompression}
Коэффициент сжатия: {len(orig_string)/len(rle_string)} {BOTTOM_DIVIDER}""")


def menu():
    while True:
        print(TOP_DIVIDER)
        print("1. Сгенерировать оригинальную строку")
        print("2. Сжать строку и сохранить в файл")
        print("3. Восстановить строку из файла и сохранить в файл")
        print("4. Вывести оригинальную строку")
        print("5. Вывести сжатую строку")
        print("6. Вывести восстановленную строку")
        print("7. Вывести отчет по сжатию")
        print("8. Выход" + BOTTOM_DIVIDER)
        choice = int(input("Введите номер пункта меню: "))
        if choice in range(1, 9):
            return choice
        else:
            print("Неверный ввод. Попробуйте еще раз.")


def print_with_divider(string):
    print(TOP_DIVIDER + string + BOTTOM_DIVIDER)


def main():
    while True:
        choice = menu()
        if choice == 1:
            hwt2.main()
        elif choice == 2:
            with open(PATH_ORIGINAL_STRING, 'r') as f:
                original_string = f.read()
            rle_list = get_rle_list_from_orig_string(original_string)
            rle_string = get_rle_string_from_rle_list(rle_list)
            save_string_to_file(PATH_RLE_STRING, rle_string)
            print_with_divider(
                "Строка успешно сжата и сохранена в файл." + PATH_RLE_STRING)
        elif choice == 3:
            with open(PATH_RLE_STRING, 'r') as f:
                rle_string = f.read()
            rle_list = get_rle_list_from_rle_string(rle_string)
            orig_string = get_orig_string_from_rle_list(rle_list)
            save_string_to_file(PATH_DECOMPRESSED_STRING, orig_string)
            print_with_divider(
                "Строка успешно восстановлена и сохранена в файл." + PATH_DECOMPRESSED_STRING)
        elif choice == 4:
            with open(PATH_ORIGINAL_STRING, 'r') as f:
                print_with_divider("Оригинальная строка: \n" + f.read())
        elif choice == 5:
            with open(PATH_RLE_STRING, 'r') as f:
                print_with_divider("Сжатая строка: \n" + f.read())
        elif choice == 6:
            with open(PATH_DECOMPRESSED_STRING, 'r') as f:
                print_with_divider("Восстановленная строка: \n" + f.read())
        elif choice == 7:
            compressions_ratio()
        elif choice == 8:
            exit()


if __name__ == "__main__":
    main()
