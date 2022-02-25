"""
Name: Darla Valderrama
hw6.py

Problem: I will be working with strings and write functions that accept arguments and return values.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    user_input = eval(input("Enter here desired integer: "))
    print("That is ${:.2f}".format(user_input))


def encode():
    user_input = input("Enter a message: ")
    number_input = eval(input("Enter a key: "))
    acc = ""
    for coding in user_input:
        i = ord(coding)
        newbie = number_input + i
        another_newbie = chr(newbie)
        acc = acc + another_newbie
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume


def sum_n(number):
    acc = 0
    for i in range(number + 1):
        acc += i
    return acc


def sum_n_cubes(number):
    acc = 0
    for i in range(number + 1):
        acc += i ** 3
    return acc


def encode_better():
    acc = ""
    one_message = input("Enter desired message here: ")
    two_message = input("Enter next desired message: ")
    for i in range(len(one_message)):
        primary = ord(one_message[i])
        secondary = ord(two_message[i])
        adding_keys = primary + secondary - 97
        acc += chr(adding_keys)
    print(acc)



if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
