"""
Name: Vinicius Nunes Lopes
bumper.py
"""

from random import randint
from time import sleep
import math
from graphics import GraphWin, Circle, Point, color_rgb

def get_random(change):
    return randint(-change, +change)

def did_collide(circ1, circ2):
    distance = math.sqrt((circ1.getCenter().getX() - circ2.getCenter().getX()) ** 2
                         + (circ1.getCenter().getY() - circ2.getCenter().getY()) ** 2)
    if distance <= circ1.getRadius() + circ2.getRadius():
        return True
    return False

def hit_vertical(circle, win):
    roof = circle.getCenter().getY() + circle.getRadius()
    floor = circle.getCenter().getY() - circle.getRadius()
    if roof >= float(win.getHeight()) or floor <= 0:
        return True
    return False

def hit_horizontal(circle, win):
    left_side = circle.getCenter().getX() - circle.getRadius()
    right_side = circle.getCenter().getX() + circle.getRadius()
    if left_side <= 0 or right_side >= float(win.getWidth()):
        return True
    return False

def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color

def bumper():

    win = GraphWin("Bumper game", 500, 500)

    ball1 = Circle(Point(randint(2, (win.getWidth()) - 2),
                         randint(2, (win.getWidth() - 2))), 20)
    ball2 = Circle(Point(randint(2, (win.getWidth()) - 2),
                         randint(2, (win.getWidth() - 2))), 20)
    ball1.setFill(get_random_color())
    ball2.setFill(get_random_color())
    ball1.draw(win)
    ball2.draw(win)

    dx1 = get_random(10)
    dy1 = get_random(10)
    dx2 = get_random(10)
    dy2 = get_random(10)
    while True:
        ball1.move(dx1, dy1)
        ball2.move(dx2, dy2)
        if hit_horizontal(ball1, win):
            dx1 = -dx1
        elif hit_horizontal(ball2, win):
            dx2 = -dx2
        elif hit_vertical(ball1, win):
            dy1 = -dy1
        elif hit_vertical(ball2, win):
            dy2 = -dy2
        elif did_collide(ball1, ball2):
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2
        sleep(0.001)

def main():
    bumper()

if __name__ == '__main__':
    main()
