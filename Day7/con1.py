import sys

type = sys.argv[1]

if type == "t2.micro":
    print("We will create t2.micro instance for you")
elif type == "t2.medium":
    print("We will create t2.medium it will cost you $2 per hour")
elif type == "t2.large":
    print("We will create t2.large it will cost you $3 per hour")
else:
    print("Please enter a valid instance type")
