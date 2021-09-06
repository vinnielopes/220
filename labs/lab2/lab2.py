"""
Name: Vinicius Nunes Lopes
lab2.py

Certification of authenticity:
I certify that this assignment is entirely my own work
"""
import math

def multiplication_table():

    for i in range (1,11):
        print( 1 * i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i, 7 * i, 8 * i, 9 * i, 10 * i)

multiplication_table()


def triangle_area():
    a = 6
    b = 6
    c = 6
    s = (a + b + c) / 2
    area = math.sqrt( s * (s-a) * (s-b) * (s-c))
    print(" area of the triangle: ", area)

triangle_area()

def sum_of_squares():
    lower = eval(input("Input lower bound: "))
    upper = eval(input("Input upper bound: "))
    for i in range(0, (upper+1)-lower):
        print(math.pow(lower+i,2))

sum_of_squares()

def power():
    base = eval(input("Input the base: "))
    exponent = eval(input("input the exponent: "))
    for i in range (exponent):
        print(base ** i)
power()


