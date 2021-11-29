"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

def binary(lst, value):
    mid = lst[len(lst)//2]

    while mid != value and len(lst) != 1:
        if value > mid:
            lst = lst[mid + 1:]
        else:
            lst = lst[:mid]

        mid = lst[len(lst)//2]

    if len(lst) == 1 and lst[0] != value:
        return False
    else:
        return True


def ss(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
            values[i], values[pos] = values[pos], values [i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()
    return dx * dy

def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    ss(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]

def sf(fn):
    file = open(fn, "r")
    signals = file.read().split()
    list_signals = []
    for i in range(len(signals)):
        if 4000 <= eval(signals[i]) <= 5000:
            list_signals.append(signals[i])
        if len(list_signals) == 5:
            print(len(list_signals))
            print(list_signals)
            print(i)
            break


def main():
    pass


main()
