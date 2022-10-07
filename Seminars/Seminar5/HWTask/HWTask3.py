# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def check_includes(word, includes):
    if includes in word:
        return True
    else:
        return False

def delete_includes_word(string, includes):
    new_string = ""
    for word in string.split():
        if not check_includes(word, includes):
            new_string += word + " "
    return new_string

def main():
    #orig_string = input("Введите строку: ")
    orig_string = "# задача 3. Напишите програмабвму, удабвляющую иабвз текстабв все слова, содержащие \"абв\". "
    print("Исходная строка: ", orig_string)
    #del_string = input("Введите слово, которое нужно удалить: ")
    del_string = "абв"
    print("Удаляемая строка: ", del_string)
    new_string = delete_includes_word(orig_string, del_string)
    print("Новая строка: ", new_string)

if __name__ == "__main__":
    main()


