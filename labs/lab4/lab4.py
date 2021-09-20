"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *

import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(190,190), Point(210,210))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)



    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        rec = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX()+10, p.getY() + 10))
        rec.setOutline("red")
        rec.setFill("red")
        rec.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked

    instructions.undraw()
    instructions.setText("Click to close program")
    instructions.draw(win)

    win.getMouse()

    win.close()



def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Build Rectangle", 400, 400)
    # # Mouse click defines opposite corners of a rectangle


    # Draws rectangle
    a = win.getMouse()
    b = win.getMouse()
    rec = Rectangle(a, b)
    rec.draw(win)

    win.getMouse()

    # Prints the perimeter and area of the rectangle

    length = abs((b.getX() - a.getX()))
    width = abs((b.getY() - a.getY()))
    area = length * width
    perimeter = 2 * (length + width)

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "Area is " + str(area) + " and perimeter is " + str(perimeter))
    instructions.draw(win)

    win.getMouse()

    inst_pt = Point(100, 390)
    instructions2 = Text(inst_pt, "Click to end the program")
    instructions2.draw(win)

    win.close()

def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4 Circle", width, height)

    pointA = win.getMouse()
    pointB = win.getMouse()

    d = math.sqrt((pointB.getX()-pointA.getX())**2 + (pointB.getY()-pointA.getY())**2)
    cir = Circle(pointA, d)
    cir.draw(win)

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "The radius is " + str(d))
    instructions.draw(win)

    inst_pt = Point(200, 320)
    instructions2 = Text(inst_pt, "Click to end the program")
    instructions2.draw(win)

    win.getMouse()
    win.close()

def pi2():
    seq = eval(input("Enter n: "))
    acc = 0
    for i in range(seq):
        nom = 4
        den = 1 + (2 * i)
        frac = ( nom / den ) * ((-1)**i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)

    pass

def main():
    # squares()
    # rectangle()
    # circle()
    pi2()


main()
