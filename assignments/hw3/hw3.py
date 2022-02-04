"""
Darla Valderrama
hw3.py

Problem: I will develop simple Python programs that use for loops while computing arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    ask_grades = eval(input("How many grades will you enter? "))
    acc = 0
    for i in range(1, ask_grades + 1):
        hw_grade = eval(input("What was your grade for hw " + str(1)))
        acc += hw_grade
    average_grade = acc / ask_grades
    print(average_grade)


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("How much do you want to donate?: "))
        acc += tip
    print(acc)


def newton():
    num_square = eval(input("What number is 'x?: "))
    improve = eval(input("How many times should we improve the approximation? "))
    prox = num_square /2
    for i in range(improve):
        prox = ((prox + (num_square / prox))/2)
    print(num_square, prox)


def sequence():
    series = eval(input("What is the number of terms in a series?: "))
    for i in range(1, series + 1):
        seq = 1 + (i // 2 * 2)
        print(seq, end=" ")


def pi():
    new_series = eval(input("What is the number of terms in a series?: "))
    acc = 1
    for i in range(new_series):
        num = 2 + ((i//2) * 2)
        den = 1 + ((i+1)//2) * 2
        fraction = num / den
        acc = acc * fraction
    print(acc * 2)


if __name__ == '__main__':
    pass
