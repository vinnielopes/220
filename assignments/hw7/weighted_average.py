"""
Name: Vinicius Nunes Lopes
weighted_average.py.py

Problem: Calculate the weighted average from a text file

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def weighted_average(in_file_name, out_file_name):
    grades = open(in_file_name, 'r')
    count = len(open(in_file_name).readlines())
    average = open(out_file_name, 'w')

    error = 0
    acc = 0
    for lines in grades:
        sum = 0
        total_w = 0
        name_grades = lines.strip("\n",).split(":")
        name = name_grades[0]
        grades = name_grades[1].strip().split()

        for i in range(0, len(grades), 2):
            number = eval(grades[i]) * eval(grades[i + 1])
            sum = sum + number
            total_w = total_w + eval(grades[i])

        if total_w == 100:
            weighted_average = sum/100
        else:
            weighted_average = 0
        acc = (acc + weighted_average)

        if total_w < 100:
            average.write(name + "'s average: Error: The weights are less than 100.\n")
            error = error + 1
        if total_w > 100:
            average.write(name + "'s average: Error: The weights are more than 100.\n")
            error = error + 1
        if total_w == 100:
            average.write(name + "'s average: " + str(round(weighted_average, 1)) + "\n")
    average.write("Class average: " + str(round((acc/(count-error)), 1)) + "\n")

def main():
    weighted_average("grades.txt", "avg.txt")

if __name__ == '__main__':
    main()
