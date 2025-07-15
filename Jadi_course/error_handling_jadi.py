"""
Error handling with 'try'
"""


def divide(a, b):
    result = a / b
    return result


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Result:", divide(num1, num2))

    except ZeroDivisionError as e:
        print("You can't divide to 0(zero)")

    except ValueError as e:
        print("Wrong input. (Please enter a numerical)")

    else:
        print("Program doing well🔥😎")
