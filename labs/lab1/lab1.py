"""
Name: <Vinicius Lopes>
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area ():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    area = length * width
    print("area =", area)

def calc_volume():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume =", volume)

def shooting_percentage():
    total_shots = eval(input("total number of shots: "))
    shots_made = eval(input("number of shots made: "))
    shooting_percentage = (shots_made/total_shots)*100
    print ("shooting percentage =", shooting_percentage,"%")

def coffee():
    coffee_cost_per_pound = 10.50
    shipping_cost_per_pound = 0.86
    fixed_overhead_cost = 1.50
    pound = eval(input("Number of pounds of coffee: "))
    total_cost = (coffee_cost_per_pound * pound) + (shipping_cost_per_pound * pound) + fixed_overhead_cost
    print("total cost =", total_cost)

def kilometers_to_miles():
    kilometer = eval(input("number of kilometers driven: "))
    conversion_from_km_to_mi = kilometer * 1.61
    print("number of miles driven =", conversion_from_km_to_mi)

kilometers_to_miles()
coffee()
shooting_percentage()
calc_rec_area()
calc_volume()