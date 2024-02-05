import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

value = input("Let's play...\n1 for rock\n2 for  paper\n3 for scissors\nEnter your choice:\n\n ")

player = int(value)

if player < 1 or player > 3: sys.exit("Oops, nonexisting choice. So let's try another one 😄.")

digital = random.choice("123")

computer = int(digital)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3: print("Congratulations! You won this time ㊗️💪😄.")
elif player == 2 and computer == 1: print("Congratulations! You won this time ㊗️💪😄.")
elif player == 3 and computer == 2: print("Congratulations! You won this time ㊗️💪😄.")
elif player == computer: print("🤝 It's a tie game .")
else: print("Python wins 💥")

    # print("Congratulations! You won this time ㊗️💪😄.")