"""
Name: Vinicius Nunes Lopes
greeting.py

Problem: To create a Happy Valentine's card

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

from time import sleep
from graphics import GraphWin, Circle, Point, Polygon, Rectangle, Text, Line

def main():
    win = GraphWin("Happy Valentine's card", 500, 500)
    win.setCoords(0, 0, 10, 10)

    # Circles in the back

    for i in range(6):
        circle_x = 0 + 2 * i
        background = Circle(Point(circle_x, 0), 2)
        background2 = Circle(Point(circle_x, 2), 2)
        background3 = Circle(Point(circle_x, 4), 2)
        background4 = Circle(Point(circle_x, 6), 2)
        background5 = Circle(Point(circle_x, 8), 2)
        background6 = Circle(Point(circle_x, 10), 2)
        background.draw(win)
        background2.draw(win)
        background3.draw(win)
        background4.draw(win)
        background5.draw(win)
        background6.draw(win)

    # Heart design
    heart_x1 = 3.5
    heart_x2 = 6.5
    heart_y = 6.5
    rad = 1.7
    color = "red"
    ratio = 0.87

    # Circle one
    circ1 = Circle(Point(heart_x1,heart_y),rad)
    circ1.setFill(color)
    circ1.setOutline(color)


    # Circle two
    circ2 = Circle(Point(heart_x2, heart_y), rad)
    circ2.setFill(color)
    circ2.setOutline(color)


    # Triangle
    triangle = Polygon(Point(heart_x1-(ratio*rad),heart_y-(rad/2)),
                       Point(heart_x2+(ratio*rad),heart_y-(rad/2)),Point(5,2))
    triangle.setFill(color)
    triangle.setOutline(color)

    # Square
    square1 = Rectangle(Point(heart_x1,heart_y),Point(heart_x2,heart_y-1))
    square1.setFill(color)
    square1.setOutline(color)

    # Happy Valentine day
    happy = Text(Point(5,6), "Happy Valentine's Day!")
    happy.setSize(29)

    # Draw heart shape
    circ1.draw(win)
    circ2.draw(win)
    triangle.draw(win)
    square1.draw(win)
    happy.draw(win)

    win.getMouse()

    happy.setSize(36)
    happy.move(0,3)

    # Draws arrow
    arrow_x3 = -1
    arrow_x4 = 1
    arrow_y5 = 6

    middle_arrow = Line(Point(arrow_x3 - 1, arrow_y5), Point(arrow_x4,arrow_y5))
    middle_arrow.setWidth(10)
    middle_arrow.draw(win)

    rec = Rectangle(Point(arrow_x3 - 0.5, arrow_y5), Point(arrow_x4 - 1.5, arrow_y5-1))
    message = Text(Point(arrow_x3, arrow_y5 - 0.5), "love you")
    message.draw(win)
    rec.draw(win)

    middle_arrow.setArrow("last")

    for _ in range(5):
        middle_arrow.move(1, 0)
        message.move(1, 0)
        rec.move(1, 0)
        sleep(0.1)

    shot = Rectangle(Point(4.6,7), Point(6, 5))
    shot.setFill("red")
    shot.setOutline("red")
    shot.draw(win)

    sleep(1)
    close_message = Text(Point(5,4), "Click anywhere to close")
    close_message.setFill("white")
    close_message.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
