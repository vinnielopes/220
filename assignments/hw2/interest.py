"""
Name: Vinicius Nunes Lopes
interest.py

Problem: To compute the monthly interest on a credit card account

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def main():

    # Ask for annual interest rate
    rate = eval(input("What is the annual interest rate for your account? "))

    # Ask for number of days in the billing cycle
    bil_days = eval(input("What is the number of days in the billing cycle? "))

    # Ask for balance
    balance = eval(input("What is your previous (net) balance? $"))

    # Multiply the net balance shown on the statement
    # by the numbers of days in the billing cycle
    net_balance = balance * bil_days

    # Ask for payment made and date
    payment = eval(input("What amount did you pay? $"))
    day = eval(input("What day of the billing cycle was the payment made?"))

    # Multiply the net payment received by the number of days
    # the payment was received before the end of the billing cycle
    step_2 = payment * (bil_days - day)

    # Subtract the result of the calculation in the step 2
    # from the result of the calculation in step 1
    step_3 = net_balance - step_2

    # Divide the result of step 3 by the number of days in the billing cycle
    # the resulting value is the average daily balance
    avg_balance = step_3 / bil_days

    # Calculate the monthly interest charge
    month_charge = avg_balance * ((rate/100)/(12))

    # Print the result
    print(round(month_charge, 2))


if __name__ == '__main__':
    main()
