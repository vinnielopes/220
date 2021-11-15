"""
Name: Vinicius Nunes Lopes
lab11.py
"""
from random import randint

def words(itn):
    infile = open(itn, "r")
    contents = infile.read()
    return contents.split("\n")

def randomword(ist):
    return ist[randint(0, len(ist)-1)]

def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)

def won(word, letters):
    x = fill(word,letters)
    if x == word:
        return True
    return False

def play():
    w = words("wordlist.txt")
    secret = randomword(w)
    incorrect = 0
    guesses = []
    current = "_" * len(secret)

    while incorrect < 7 and won(secret, guesses) == False:
        display = fill(secret, guesses)
        print("Word is: ", display)
        print("Guessed letters: ", guesses)
        letter = input("Enter letter:")
        while letter in guesses:
            letter = input("Enter another letter:")
        guesses.append(letter)
        display = fill(secret, guesses)
        if display == current:
            incorrect += 1
        else:
            current = display
    if current == secret:
        print("You win!")
    else:
        print("You lost!")

def main():
    play()
    # add other function calls here
    pass


main()
