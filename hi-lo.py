print("Can you play with me a guessing game?")
input("Press ENTER to start")
low = 1
high = 1000
number_to_guess = input("Enter your number you want me to guess "
                        "from {} to {}: ".format(low, high))
number_of_guesses = 1
# while True: # While True là vòng lặp vô tận không điều kiện trừ khi có break
while low != high:
    guess = low + (high - low) // 2
    reply = input("My guess is {}. Should I guess higher or lower?\n"
                  "Enter h or l, or c if my guess was correct: ".format(guess)).casefold()
    # casefold dùng để đưa về chữ viết thường
    if reply != "c":
        number_of_guesses += 1
        if reply == "h":
            low = guess
        elif reply == "l":
            high = guess
        else:
            print("Please enter h, l or c")
    else:
        print("Good for me, I'm correct and this is the number of times I've guessed:")
        print(number_of_guesses)
        break
else:
    print("My final guess is {}. Am I correct?".format(high))
    answer = input("Y or N?").casefold()
    if answer == "y":
        print("Good for me, I'm correct and this is the number of times I've guessed:")
        print(number_of_guesses)
    else:
        print("You're fooling me")
