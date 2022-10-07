# задача 4 необязательная Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os
import re

PATH_POLYNOMIAL1 = "Seminars/Seminar5/HWTask/HWT4_polynomial1.txt"
PATH_POLYNOMIAL2 = "Seminars/Seminar5/HWTask/HWT4_polynomial2.txt"
PATH_POLYNOMIAL = "Seminars/Seminar5/HWTask/HWT4_polyn_result.txt"

def read_polynomial(path):
    with open(path, "r") as f:
        polynomial = f.read()
    return polynomial

def write_polynomial(path, polynomial):
    with open(path, "w") as f:
        f.write(polynomial)

def get_Coefficient(polynomial):
    return int(polynomial.split("*x")[0])

def get_Degree(polynomial):
    if "x" in polynomial:
        if "^" in polynomial:
            return int(polynomial.split("^")[1])
        else:
            return 1
    else:
        return 0

def get_element_list(polynomial):
    element_list = []
    element = ""
    for i in range(len(polynomial)):
        if polynomial[i] == "+":
            element_list.append(element)
            element = ""
        elif polynomial[i] == "-":
            element_list.append(element)
            element = "-"
        else:
            element += polynomial[i].strip()
    element_list.append(element)
    return element_list

def get_polinomial_dict(polynomial):
    polynomial_dict = {}
    polynomial = get_element_list(polynomial)
    for i in polynomial:
        polynomial_dict[get_Degree(i)] = get_Coefficient(i)
    return polynomial_dict

def get_sum_polynomial(polynomial1, polynomial2):
    polynomial1_dict = get_polinomial_dict(polynomial1)
    polynomial2_dict = get_polinomial_dict(polynomial2)
    polynomial_dict = {}
    for i in polynomial1_dict:
        if i in polynomial2_dict:
            polynomial_dict[i] = polynomial1_dict[i] + polynomial2_dict[i]
        else:
            polynomial_dict[i] = polynomial1_dict[i]
    for i in polynomial2_dict:
        if i not in polynomial1_dict:
            polynomial_dict[i] = polynomial2_dict[i]
    return polynomial_dict

def sort_dict_by_key(polynomial_dict):
    return {k: polynomial_dict[k] for k in sorted(polynomial_dict, reverse=True)}

def get_polynomial(polynomial_dict):
    polynomial = ""
    for i in polynomial_dict.keys():
        if polynomial_dict[i] > 0:
            polynomial += f"+{polynomial_dict[i]}*x^{i}"
        elif polynomial_dict[i] < 0:
            polynomial += f"{polynomial_dict[i]}*x^{i}"
    if polynomial[0] == "+":
        polynomial = polynomial[1:]
    if polynomial == "":
        polynomial = "0"
    if polynomial[-2:] == "^0":
        polynomial = polynomial[:-4]
    return polynomial.strip()


def main():
    polynomial1 = read_polynomial(PATH_POLYNOMIAL1)
    polynomial2 = read_polynomial(PATH_POLYNOMIAL2)
    polynomial_dict = get_sum_polynomial(polynomial1, polynomial2)
    polynomial_dict = sort_dict_by_key(polynomial_dict)
    polynomial = get_polynomial(polynomial_dict)
    write_polynomial(PATH_POLYNOMIAL, polynomial)

if __name__ == "__main__":
    main()
