age = int(input("How old are you? "))
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("enjoy your free time")

print("-" * 90)
if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("Have a good day a work")