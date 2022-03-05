"""
Name: Darla Valderrama
hw7.py

Problem: In this program I will be writing functions, reading and writing text files.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + str(word) + "\n")
            i += 1
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts_file = line.split()
        wage = float(parts_file[2])
        wage += 1.65
        wage = wage * int(parts_file[3])
        outfile.write(str(parts_file[0] + " " + str(parts_file[1]) + " " + str(wage) + "\n"))
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        positions_value = 10 - i
        acc += int(isbn[i]) * positions_value
    return acc


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()


def encode():
    user_input = input("Enter a message: ")
    number_input = eval(input("Enter a key: "))
    acc = ""
    for coding in user_input:
        i = ord(coding)
        newbie = number_input + i
        another_newbie = chr(newbie)
        acc = acc + another_newbie
    return acc


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    outfile = open(friend_name, "w+")
    for line in infile:
        outfile.write(encode(line, key))
    infile.close()
    outfile.close()



def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file_pad = open(pad_file_name, "r")
    key_file = pad_file_name.read()
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key_file))
    infile.close()
    key_file.close()
    outfile.close()



if __name__ == '__main__':
    pass
