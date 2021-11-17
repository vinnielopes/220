"""
Name: Vinicius Nunes Lopes
threeDoorGame.py
"""
from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button

def main():
    win = GraphWin("Three Button Game", 400, 400)
    win.setCoords(0, 0, 10, 10)

    shape1 = Rectangle(Point(1, 6), Point(3, 4))
    door1 = Button(shape1, "Door 1")
    door1.draw(win)

    shape2 = Rectangle(Point(4, 6), Point(6, 4))
    door2 = Button(shape2, "Door 2")
    door2.draw(win)

    shape3 = Rectangle(Point(7, 6), Point(9, 4))
    door3 = Button(shape3, "Door 3")
    door3.draw(win)

    secret_door_message = Text(Point(5, 8), "I have a secret door!")
    secret_door_message.setSize(20)
    secret_door_message.draw(win)

    # Asks user to click on a door
    instruction = Text(Point(5,2), "Click to choose my door!")
    instruction.setSize(15)
    instruction.draw(win)

    # Gets input from user
    rand = randint(0, 2)
    list_0 = [door1, door2, door3]
    list_1 = ["Door 1", "Door 2", "Door 3"]
    random_door = list_0[rand]
    random_door_str = list_1[rand]

    door_clicked = win.getMouse()

    if random_door.is_clicked(door_clicked):
        secret_door_message.setText("You Win!")
        random_door.color_button("green")
        instruction.setText("Click to close!")
    else:
        secret_door_message.setText("You Lost!")
        instruction.setText("{0}".format(random_door_str) + " is my secret door! \n \n"
                                                            "Click to close!")
        if door1.is_clicked(door_clicked):
            door1.color_button("red")
        elif door2.is_clicked(door_clicked):
            door2.color_button("red")
        elif door3.is_clicked(door_clicked):
            door3.color_button("red")

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
