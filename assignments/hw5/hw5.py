"""
Name: Darla Valderrama
hw5.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    user_input = input("Enter a name (first-last order): ")
    first_name = user_input.split()[0]
    last_name = user_input.split()[1]
    print(last_name + ", " + first_name)


def company_name():
    user_input = input("Enter a three-part domain: ")
    task = user_input.split(".")
    print(task[1])


def initials():
    user_input = eval(input("How many students are in a class?: "))
    for i in range(1, user_input + 1):
        first_name = str(input("Enter the first name of the student " + str(i) + ":"))
        last_name = str(input("Enter" + first_name + "'s last name of the student: "))
        print(first_name + "'s initials are: " + first_name[0] + last_name[0])


def names():
    user_input = input("Enter a list of names: ")
    user_input = user_input.split(", ")
    for name in user_input:
        first_name = name.split(" ")[0]
        last_name = name.split(" ")[1]
        print(first_name[0] + last_name[0], end=" ")


def thirds():
    user_input = eval(input("Enter the number of sentences: "))
    for i in range(user_input):
        second_input = input("Enter sentence " + str(i+1) + " here: ")
        for x in range(2, len(second_input), 3):
            print(second_input[x], end=" ")


def word_average():
    acc = 0
    user_input = input("Enter a sentence: ")
    user_input = user_input.split(" ")
    for wordy in user_input:
        acc = acc + len(wordy)
    print(acc / len(user_input))


def pig_latin():
    user_input = input("Enter a sentence to convert to pig latin: ")
    user_input = user_input.lower()
    user_input = user_input.split(" ")
    for wordy in user_input:
        piggy = wordy[1:]
        piggy = piggy + wordy[0] + "ay "
        print(piggy.rstrip())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    # pass
