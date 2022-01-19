"""
Name: Darla Valderrama
hw1.py

Problem: I will be implementing and executing Python programs as I do arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    total = shots_made / total_shots * 100
    print("Shooting Percentage: ", total, "%")


def coffee():
    cafe = eval(input("How many pounds of coffee would you like?: "))
    coffee_costs = ((10.50 + 0.86) * cafe) + 1.50
    print("You're total is: ", coffee_costs)


def kilometers_to_miles():
    john = eval(input("How many kilometers did you travel?: "))
    miles = john / 1.61
    print("That's ", miles, "miles!")


if __name__ == '__main__':
    pass
