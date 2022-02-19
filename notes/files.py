"""
Reading and Writing Files :

open(filename, mode)
"r" = read
open("data.txt", "r")

3 ways can read files: getting txt out of a file
(1) my_file.read()
# return single str that is the entire file, if a whole book, book will be stored in that variable

(2) my_file.readline()
# returns a string that is just one single line --> will include a new line character "__/n"

(3) my_file.readlines()
# returns a list of all the lines in the file w new lines at the end --> ["___/n", "__/n", ..]


"w" = write
"""


def print_poem():
    my_poem = open('poem.txt', 'r')
    poem_text = my_poem.read()
    print(poem_text)
    my_poem.close()


def print_file_lines():
    my_poem = open('poem.txt', 'r')
    for i in range(5):
        line = my_poem.readline()
        print(line[:-1])    # go to the end but minus one or, starting from zero and the end minus one -1
        print(line, end=" ")


def print_file_list():
    my_poem = open('poem.txt', 'r')
    for line in my_poem.readlines():
        print(line)
print_file_list()

output_file = open('output.txt', 'w')   # in order to write in file, use w mode
print("hello world", file=output_file)
