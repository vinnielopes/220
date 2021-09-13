"""
Name: Vinicius Nunes Lopes
lab3.py

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def average():
    number = eval(input("How many homeworks did you have: "))
    acc = 0
    for i in range (1, number + 1):
        grade = eval(input("Enter grade on HW"+ str(i) + ":"))
        acc = acc + grade

    average = acc/number
    print("The average is", average)
    print()

average()

def tip_jar():
    number = 5
    acc = 0
    for i in range(1, 6):
        tip = eval(input("Tip " + str(i) + ": $" ))
        acc = acc + tip

    print("The $ amount on the tip jar is $", acc)
    print()

tip_jar()


def newton():
    x = eval(input("square root of: "))
    refine = eval(input("number of times to refine:"))
    approx = x/2

    for i in range(0,refine + 1):
        approx = (approx + (x/approx))/2

    print(approx)
    print()

newton()

def sequence():
    seq = eval(input("How many numbers in a sequence: "))
    for i in range(1, seq+1):
        number_seq = 1 + (i//2 * 2)
        print(number_seq, end="\t")

    print()
    print()

sequence()

def pi():
    seq = eval(input("How many numbers in a sequence: "))
    acc = 1
    for i in range(1, seq + 1):
        nom = 2 + ((i - 1)//2 * 2)
        den = 1 + (i//2 * 2)
        frac = nom / den
        acc = acc * frac
    print(acc*2)

pi()




# average()
# newton()
# sequence()
