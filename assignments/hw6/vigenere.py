"""
Name: Vinicius Nunes Lopes
vigenere.py

Problem: Use vigenere cipher in a message

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import GraphWin, Text, Point, Rectangle, Entry

def drawtext(a, b, message, Win):
    text_info = Text(Point(a, b), message)
    text_info.draw(Win)

def main():
    win = GraphWin("Main window", 400, 200)
    win.setCoords(0, 0, 10, 10)

    # Message to code box
    drawtext(2, 7, "Message to code", win)
    input = Entry(Point(5, 7), 20)
    input.draw(win)

    # Keyword box
    drawtext(2, 6, "Enter Keyword", win)
    input_code = Entry(Point(5, 6), 20)
    input_code.draw(win)

    # Encode box
    encode_outline = Rectangle(Point(4, 4), Point(6, 3))
    encode_outline.draw(win)
    position = encode_outline.getCenter()
    encode_box = Text(position, "Encode")
    encode_box.draw(win)

    win.getMouse()

    # Undraw encode box
    encode_outline.undraw()
    encode_box.undraw()

    # Blank output
    output_text = Text(Point(5, 3), "")
    output_text.draw(win)

    # Storing the message
    message_list = []
    keywordStr = input.getText().replace(" ", "").upper()
    for letter in keywordStr:
            message_list.append(letter)
    print(message_list)

    # Storing the code
    code_list = []
    codeStr = input_code.getText().upper()
    for i in range(len(codeStr)):
        code_list.append(ord(codeStr[i])-65)

    while len(keywordStr) - len(code_list) > 0:
        for i in range(len(codeStr)):
            code_list.append(ord(codeStr[i]) - 65)

    print(code_list)

    output_list = []
    for i in range(min(len(code_list),len(message_list))):
        l = ord(message_list[i]) - 65
        enc = l + code_list[i]
        enc = enc % 26
        output_list.append(chr(enc + 65))

    print(output_list)

    # Resulting message
    resulting_message = Text(Point(5, 4), "Resulting Message")
    resulting_message.draw(win)
    output_text.setText(output_list)

    # Click Anywhere to Close Window
    click_close = Text(Point(5, 1), "Click Anywhere to Close Window")
    click_close.draw(win)

    win.getMouse()

def code(message, keyword):
    # Storing the message
    message_list = []
    keywordStr = message.replace(" ", "").upper()
    for letter in keywordStr:
        message_list.append(letter)

    # Storing the code
    code_list = []
    codeStr = keyword.upper()
    for i in range(len(codeStr)):
        code_list.append(ord(codeStr[i]) - 65)

    while len(keywordStr) - len(code_list) > 0:
        for i in range(len(codeStr)):
            code_list.append(ord(codeStr[i]) - 65)

    output_list = []
    for i in range(min(len(code_list), len(message_list))):
        l = ord(message_list[i]) - 65
        enc = l + code_list[i]
        enc = enc % 26
        output_list.append(chr(enc + 65))

    return "".join(output_list)

if __name__ == '__main__':
    main()
