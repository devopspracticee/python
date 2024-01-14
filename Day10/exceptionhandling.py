import sys

num1 = sys.argv[1]
num2 = sys.argv[2]


try:
    div = int(num1) / int(num2)
    print("The division of " + num1 + " and " + num2 + " is:", div)
except ZeroDivisionError:
    print("Enter a valid number other than zeros")
