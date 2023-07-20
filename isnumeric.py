number = input("Please enter a series of numbers, using any seperators you like: ")
seperator = ""

for char in number:
    if not char.isnumeric():
        seperator = seperator + char

#print(seperator)
value = "".join(char if char not in seperator else " " for char in number).split()
print(sum([int(val) for val in value]))
