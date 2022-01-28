"""
Darla Valderrama
hw2.py

Problem: I will develop simple Python programs that create inputs/outputs do arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def sum_of_threes():
    user = eval(input("Enter an upper bound: "))
    acc = 0
    for i in range(0, user + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for my_mt in range(1, 11):
            print(i * my_mt, end=" ")
            print()


def triangle_area():
    a_tri = eval(input("Enter side a length: "))
    b_tri = eval(input("Enter side b length: "))
    c_tri = eval(input("Enter side c length: "))
    x_equa = (a_tri + b_tri + c_tri) / 2
    area = math.sqrt(x_equa*(x_equa-a_tri)*(x_equa-b_tri)*(x_equa-c_tri))
    print("Area is:", area)


def sum_squares():
    a_sq = eval(input("Enter lower range: "))
    b_sq = eval(input("Enter upper range: "))
    acc = 0
    for i in range(a_sq, b_sq + 1):
        square = i ** 2
        acc = acc + square
    print(acc)


def power():
    base = eval(input("Enter a base: "))
    expo = eval(input("Enter a exponent: "))
    acc = 1
    for i in range(expo):
        acc = acc * base
    print(acc)


if __name__ == '__main__':
    pass
