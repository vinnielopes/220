"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from random import randint


def fart(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Vinicius"
    except:
        pass


def read_data(inf):
    f = open(inf, "r")
    data = f.read()
    data = data.split()
    return data


def iil(value, list_of_values):
    i = 0
    while i < len(list_of_values):
        if list_of_values[i] == value:
            return True
        i += 1
    return False


def gi():
    x = eval(input("Enter a number: "))
    while x < 1 or x > 10:
        x = eval(input("Enter a number: "))

    return x


def nd():
    num = eval(input("Enter a number: "))
    while num >= 1:
        digits = 0
        while num != 0:
            num = num // 10
            digits += 1
        print("There are ", digits, " in the number")
        num = eval(input("Enter a number"))


def hlg():
    secret = randint(1, 100)
    guesses = 1
    num = eval(input("Guess a number: "))
    print(secret)

    while secret != num and guesses < 8:
        guesses += 1
        if num > secret:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")
        num = eval(input("Guess a number: "))

    if num != secret or guesses > 8:
        print("You lost!")
    else:
        print("You win!")


def main():
    fart([2, 3, 4, 5, 6, 7], 2)
    read_data("dataSorted.txt")
    iil(1, [2, 3, 4, 5, 6, 7])
    gi()
    nd()
    hlg()

    pass


main()
