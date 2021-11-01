"""
Name: Vinicius Nunes Lopes
lab9.py
"""
from graphics import *
import math

def addTen(nums):
    list = nums
    for i in range(0, len(list)):
        list[i] = list[i] + 10

def squareEach(nums):
    list = nums
    for i in range(0, len(list)):
        list[i] = list[i] ** 2
        # print(list)

def sumList(nums):
    list = nums
    acc = 0
    for i in range(0, len(list)):
        acc += list[i]
        # print(acc)
    return acc

def toNumbers(nums):
    list = nums
    for i in range(len(list)):
        list[i] = float(list[i])

def writeSumOfSquares():
    name_file = input("Enter file to be opened: ")
    out_file_name = input("How would you like your file to be named? ")
    infile = open(name_file, "r")
    outfile = open(out_file_name, "w")

    for line in infile:
        number = line.split()
        toNumbers(number)
        squareEach(number)
        num_sum = sumList(number)
        outfile.write("the sum of squares is: " + str(num_sum) + "\n")

def starter():
    weight = eval(input("Enter player's weight: "))
    numWins = eval(input("Enter player's number of wins: "))

    if weight >= 150 and weight < 160:
        if numWins > 5:
            print("Starter")
    elif weight > 199 or numWins > 20:
        print("Starter")
    else:
        print("Not a starter")

def leap_year(year):
    if not(year % 100 == 0) or (year % 400 == 0):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")

def circleoverlap():
    win = GraphWin("Circle stuff", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    dist_circles = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if dist_circles <= r + r2:
        message = Text(Point(200, 200), "This circles overlap")
        message.draw(win)
    else:
        message = Text(Point(200, 200), "This circles do not overlap")
        message.draw(win)


    win.getMouse()
    win.close()


def main():
    addTen([5, 2, -3])
    squareEach([5, 2, -3])
    sumList([5, 2, -3])
    toNumbers(["3", "5.7", "2"])
    starter()
    leap_year(2000)
    circleoverlap()
    writeSumOfSquares()
    pass


main()
