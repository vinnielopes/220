"""
Name: Vinicius Nunes Lopes
lab5.py
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    a = win.getMouse()
    b = win.getMouse()
    c = win.getMouse()

    # Draws the triangle
    l1 = Line(a,b)
    l2 = Line(b,c)
    l3 = Line(c,a)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)

    s1 = math.sqrt((a.getX() - b.getX()) ** 2 + (a.getY() - b.getY()) ** 2)
    s2 = math.sqrt((b.getX() - c.getX()) ** 2 + (b.getY() - c.getY()) ** 2)
    s3 =math.sqrt((a.getX() - c.getX()) ** 2 + (a.getY() - c.getY()) ** 2)


    win.getMouse()

    # Calculate the perimeter
    per = s1 + s2 + s3

    # Calculate the area
    area = math.sqrt(per * (per - s1) * (per - s2) * (per - s3))
    win.getMouse()



    message_per = Text(Point(200, 360), "the perimeter is: " + str(per))
    message_per.draw(win)

    message_area = Text(Point(200, 380), "the perimeter is: " + str(area))
    message_area.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    color = "white"
    win.setBackground(color)

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)
    shape.setFill("white")

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    r = Entry(Point(win_width/ 1.8, win_height / 2 + 40), 10)
    r.draw(win)
    g = Entry(Point(win_width/ 1.8, win_height / 2 + 70), 10)
    g.draw(win)
    b1 = Entry(Point(win_width/ 1.8, win_height / 2 + 100), 10)
    b1.draw(win)


    for i in range(5):
        red = int(r.getText())
        green = int(g.getText())
        blue = int(b1.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    z = input("Enter string here: ")
    print(z[0])

    print(z[-1])

    print(z[2:6])

    print(z[0]+z[-1])
    for i in range(len(z)):
        print(z[0:3])
    for c in z:
        print(c)

    print(len(z))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]

    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1]
    for i in range(5):
        print(x, end="")
    print()

    x = [values[2],values[3],values[4]]
    print(x)

    x = [values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[5])]
    print(x)

    x = values[0] + values[2] + float(values[5])
    print(x)

    x = len(values)
    print(x)

def another_series():
    n = str(eval(input("Enter number of terms: ")))
    acc = 0

    for i in range(0,n):
        y = 2 + (2 * (i % 3))
        acc = acc + y
        print (y, end=" ")
    print()
    print("sum = " + str(acc))


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    # another_series()
    pass


main()
