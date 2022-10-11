from encodings.utf_8 import encode
from json import encoder
import random

PATH = "Seminars/Seminar6/HWTask/football.txt"

commands = ['Спартак', 'Зенит', 'Локомотив']
#, 'Динамо', 'Торпедо', "Факел"]

def generate_matches(commands):
    with open(PATH, 'w', encoding= 'utf-8') as file:
        for i in range(len(commands)):
            for j in range(i + 1, len(commands)):
                file.write(f"{commands[i]};{random.randint(0,5)};{commands[j]};{random.randint(0,5)}"+'\n')
            
generate_matches(commands)
