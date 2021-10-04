"""
Name: Vinicius Nunes Lopes
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first_lastname = input("Type your first and last name: ")
    first_lastname.split()
    first_lastname = first_lastname.split()
    print(first_lastname[1],",", first_lastname[0])

def company_name():
    company_web = input("Enter website for a company: ")

    company_web.split(".")
    company_web = company_web.split(".")

    print(company_web[1])

def initials():
    num = eval(input("How many students are there in a class? "))

    for i in range(1,num + 1):
        first_name = input("Enter the first name of student " + str(i) + ":")
        last_name = input("Enter " + first_name + "'s last name:")
        print(first_name + "'s intials are " + first_name[0] + last_name[0])

def names():
    names_list = input("Enter a list of names here: ")
    names_list = names_list.split(", ")

    print(names_list)
    for name in names_list:
        one_name = name.split()
        initials = one_name[0][0] + one_name[1][0]
        print(initials, end=" ")

def thirds():
    number = eval(input("Enter the number of sentences: "))
    for i in range(0,number):
        print()
        sentence = input("Enter sentence " + str(i) + ":")
        for j in range(int(len(sentence)/3)):
            print(sentence[j*3], end="")


def word_average():
    acc = 0
    sentence = input("Enter a sentence here: ")
    sentence = sentence.split()

    for word in sentence:
        acc = acc + len(word)

    average = acc/len(sentence)
    print(average)

def pig_latin():
    code = input("Enter something a pig would say: ")
    code = code.lower()
    code = code.split()

    for word in code:
        pig_says = word[1:] + word[0] + "ay"
        print(pig_says, end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
