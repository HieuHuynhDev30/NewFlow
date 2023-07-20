parrot =  "Norweiguan Blue"
letter = input("Enther a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():  # hàm casefold() biến chữ hoa thành chữ thường trong string
    print("But I want to go to the cinema")
else:
    print("Me too")