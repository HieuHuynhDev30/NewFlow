name = input("Please enter your name: ")
age = int(input("Please enter your age:  "))
if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    if age < 18:
        print("Sorry {0}, you can go on the holiday {1} years later".format(name, 18 - age))
    else:
        print("Sorry {0}, this holiday is not for you".format(name))
