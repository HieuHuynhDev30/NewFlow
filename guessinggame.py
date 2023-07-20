import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
# xóa số đúng sau mỗi lần thử nếu không nó chỉ hiện thị 1 số từ lần đầu cho những lần sau
guess = int(input("Please guess number between 1 and {}: ".format(highest)))
if guess == answer:
    print("You got it first time")
else:
    while guess != answer:
        if guess > answer:
            guess = int(input("Please guess lower: "))
        elif guess < answer:
            guess = int(input("Please guess higher: "))
    print("Well done, you got it")
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     elif guess < answer:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you got it")
#     else:
#         print("Sorry, you have not guessed it")
