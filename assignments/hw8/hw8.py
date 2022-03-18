"""
Name: Darla Valderrama
hw8.py

Problem: We are using conditional control structures as well as practicing accumulations.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
        return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    infile = input("Enter name of input file with at least 2 #'s: ")
    outfile = input("Enter name of output file: ")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in readfile:
        nums = line.split()
        to_numbers(nums)
        square_each(nums)
        summation = sum_list(nums)
        writefile.write("Sum of squares = " + str(summation))


def starter(weight, wins):
    weight = eval(input("Enter weight: "))
    wins = eval(input("Enter wins: "))
    if 150 <= weight < 160 and wins >=5:
        print("Earned a starter position!")
    elif weight > 199 or wins > 20:
        print("Earned a starter position!")
    else:
        print("Did not earn a start position.")


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)

    circle_one.setFill("light blue")
    circle_one.draw(win)
    centered = win.getMouse()
    circumference_point = win.getMouse()

    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    second_circle = Circle(center, radius)
    second_circle.setFill("light blue")
    second_circle.draw(win)
    over_msg = Text(Point(2, 6), "The circles overlap!")
    over_msg.setTextColor("red")
    over_msg.setSize(10)
    do_not_over_msg = Text(Point(4, 7), "The circles do not overlap!")
    do_not_over_msg.setTextColor("red")
    do_not_over_msg.setSize(10)
    closing = Text(Point(5, 7), "Click to close")
    closing.draw(win)

    if did_overlap(circle_one, second_circle):
        over_msg.draw(win)
    else:
        do_not_over_msg.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, second_circle):
    distance = math.sqrt(math.pow(second_circle.getCenter().getX() - circle_one.getCenter().getX(), 2) +
                         math.pow(second_circle.getCenter().getY() - circle_one.getCenter().getY(), 2))
    if distance <= circle_one.getRadius() + second_circle.getRadius():
        return True
    return False


if __name__ == '__main__':
    pass
