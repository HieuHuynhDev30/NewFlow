options = ["Exit", "Learn web", "Learn hacking", "Go shopping", "Go to the cinema", "Go for a date",
           "Do exercise"]
please = "Please choose your option from the list below:"
menu = """
1. Learn web
2. Learn hacking
3. Go shopping
4. Go to the cinema
5. Go for a date
6. Do exercise
0. Exit"""
print(please, menu)
your_choice = 1
while your_choice != 0:
    if your_choice in range(0, 7):
        your_choice = int(input("Enter a number from 0 to 6 for your option from the list: "))
    else:
        your_choice = int(input(
            "Your choice is invalid, please choose again from the menu below {}\nYour choice is: ".format(
                menu)))
    if your_choice in range(1, 7):
        print("So you want to {}, then do it".format(options[your_choice]))
else:
    print("You chose {}, so you don't want to do anything. Bye!".format(options[your_choice]))
