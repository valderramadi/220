from random import randint


def get_words(file_name):
    file = open(file_name, 'r')
    read_words = file.read()
    return read_words.split('\n')


def get_random_word(words):
    wordy = words[randint(0, len(words)-1)]
    return wordy


def letter_in_secret_word(letter, secret_word):
    letter_word = ["_"] * len(secret_word)
    for letters in letter:
        for w in range(len(secret_word)):
            if secret_word[w] == letters:
                letter_word[w] = letters
    return "".join(letter_word)


def already_guessed(letter, guesses):
    if guesses == letter:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    message = []
    for m in secret_word:
        message.append("_ ")
    for t in range(len(guesses)):
        for w in range(len(secret_word)):
            if secret_word[w] == guesses[t]:
                message[w] = guesses[t] + " "
    return "".join(message)


def won(guessed):
    for i in guessed:
        if i == "_":
            return False
    return True



def play_graphics(secret_word):
    width = 700
    height = 700
    win = GraphWin("Hangman", width, height)
#     deleted code because tests were not running (emailed)





def play_command_line(secret_word):
    letters_user = []
    guessed_user_needs = 5
    while guessed_user_needs > 0 and not won(make_hidden_secret(secret_word, letters_user)):
        print("Already guessed: ", letters_user)
        print("Guesses remaining:", guessed_user_needs)
        guesses_now = input("Guess a letter now: ")
        if not already_guessed(guesses_now):
            letters_user.append()
            if not letter_in_secret_word(secret_word):
                guessed_user_needs = guessed_user_needs - 1
    if won(make_hidden_secret(secret_word, letters_user)):
        print("You're a winner! :)")
        print(secret_word)
    else:
        print("Sorry, you lost tis time! :(")
        print(secret_word)



if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
