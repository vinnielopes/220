"""
Name: Vinicius Nunes Lopes
lab2.py

Certification of authenticity:
I certify that this assignment is entirely my own work
"""
import math

def sum_of_three():
    number = eval(input("Input an upper bound: "))
    sum = 0
    for x in range(0, number -1, 3):
        a = 3 + x
        sum = sum + a

    print(sum)

sum_of_three()

def multiplication_table():
    y = eval(input("Choose a multiple: "))
    y = y + 1
    for row in range(1, y):
        # print(i,":", 1 * i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i, 7 * i, 8 * i, 9 * i, 10 * i)
        print(row, ":", end=" ")
        for col in range(1,y):
            print (row * col, end="\t")
        print()

multiplication_table()


def triangle_area():
    a = eval(input("Input the length of side a: "))
    b = eval(input("Input the length of side b: "))
    c = eval(input("Input the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt( s * (s-a) * (s-b) * (s-c))
    print(" area of the triangle: ", area)

triangle_area()

def sum_of_squares():
    lower = eval(input("Input lower bound: "))
    upper = eval(input("Input upper bound: "))
    sum = 0
    for i in range(0, (upper+1)-lower):
        square = math.pow(lower+i,2)
        sum = sum + square

    print(sum)

sum_of_squares()

def power():
    base = eval(input("Input the base: "))
    exponent = eval(input("input the exponent: "))
    number = 1
    for i in range(exponent):
        number = number * base

    print(base, "^", exponent, "=", number)

power()


