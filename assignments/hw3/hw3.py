"""
Name: Vinicius Nunes Lopes
hw3.py

Problem: To calculate different means

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

import math
def main():

    # Insert numbers
    num = eval(input("Enter the values to be entered: "))
    acc1 = 0
    acc2 = 0
    acc3 = 1

    for i in range(num):
        inp = eval(input("Enter value: "))
        acc1 = acc1 + (inp**2)
        acc2 = acc2 + 1/inp
        acc3 = acc3 * inp

    # RMS average
    rms = math.sqrt(acc1 / num)
    print(round(rms,3))

    # Harmonic mean
    harm = num / acc2
    print(round(harm,3))

    # Geometric mean
    geo = acc3 ** (1./num)
    print(round(geo,3))

if __name__ == '__main__':
    main()