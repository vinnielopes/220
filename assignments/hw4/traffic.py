"""
Name: Vinicius Nunes Lopes
traffic.py

Problem: To help DOT with average number of cars in the road

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def main():
    acc1 = 0
    num = eval(input("How many roads were surveyed? "))
    for i in range(1,num + 1):
        acc = 0
        days = eval(input("How many days was road " + str(i) + " surveyed? "))
        for j in range(1, days + 1):
            cars = eval(input("How many cars travelled on day " + str(j) + " ? "))
            acc = acc + cars
            acc1 = acc1 + cars
            average = acc/days
        print("Road " + str(i) + " average vehicles per day: " + str(round(average, 2)))
    avg_cars_road = acc1/num
    print("Total number of vehicles traveled on all roads: " + str(round(acc1, 2)))
    print("Average number of vehicles per road: " + str(round(avg_cars_road, 2)))

if __name__ == '__main__':
    main()
