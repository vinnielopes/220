"""
Name: Vinicius Nunes Lopes
lab8.py
"""

def number_words(in_name, out_name):
    infile = open(in_name, "r")
    outfile = open(out_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + "\n")
            i = i + 1

def hw(inname, outname):
    infile = open(inname, "r")
    outname = open(outname, "w+")

    for line in infile:
        puts = line.split()
        wage = eval(puts[2]) + 1.65
        total_wage = wage * eval(puts[3])
        outname.write(puts[0]+ " " + puts[1] + " " + str(wage) + " " + str(total_wage) + "\n")

def isbn(isbn_str):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc = acc + (eval(isbn_str[i]) * position)
    return acc

def sm(file, friend):
    infile = open(file, "r")
    outfile = open(friend+".txt", "w+")
    for line in infile:
        outfile.write(line)

def encode(message, integer_value):
    acc = ''
    for i in range(len(message)):
        number = ord(message[i])
        letter = chr(number + integer_value)
        acc = acc + letter
    return acc

def ssn(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        new = encode(line, key)
        outfile.write(new)

def ssu(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    padfile = open(pad, "r")
    key = padfile.read()
    for line in infile:
        new = encode_better(line, padfile)
        outfile.write(new)


def main():
    number_words("Walrus.txt", "count.txt")
    hw("hourly_wages.txt", "raised_hourly_wages")
    isbn("0012345678")
    sm("message.txt", "bob")
    ssn("safest_message.txt", "bianca", 1)
    ssu("safest_message.txt", "robert", "pad.txt")
    pass


main()
