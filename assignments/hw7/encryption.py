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
