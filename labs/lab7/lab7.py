"""
Name: Vinicius Nunes Lopes
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math
def cash_conversion():
    integer = eval(input("Enter an integer: "))
    one = str(integer // 1)
    two = str(integer % 1)

    print("${:2}".format(one,".",two))

def encode():
    code = input("Enter your message:")
    integer_value = eval(input("Enter integer key value: "))
    for i in range(len(code)):
        number = ord(code[i])
        letter = chr(number + integer_value)
        print(letter, end="")

def sphere_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

def sphere_volume(radius):
    sphere_volume = 4/3 * math.pi * (radius ** 3)
    return sphere_volume

def main():
    cash_conversion()
    encode()
    sphere_area()
    sphere_volume()
    pass


main()
