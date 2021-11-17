"""
Name: Vinicius Nunes Lopes
Button.py
"""
from graphics import Text
class Button:
    """
    This class draws a shape with a message at the center
    """
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        """
        Returns the label that is displayed on the button
        """
        return self.text.getText()

    def draw(self, win):
        """
        Draws the button (rectangle + message)
        """
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """
        Undraws the button (rectangle + message)
        """
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """
        Returns a boolean whether the a button has been clicked
        """
        x_1 = self.shape.getP1().getX()
        x_2 = self.shape.getP2().getX()
        p_x = point.getX()

        y_1 = self.shape.getP1().getY()
        y_2 = self.shape.getP2().getY()
        p_y = point.getY()
        return x_1 <= p_x <= x_2 and y_1 <= p_y <= y_2

    # >x>
    # or split them up

    def color_button(self, color):
        """
        Sets the button to an specific color
        """
        self.shape.setFill(color)

    def set_label(self, new_label):
        """
        Sets label to the label
        """
        self.text.setText(new_label)
