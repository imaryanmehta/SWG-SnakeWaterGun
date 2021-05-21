# Snake Water Gun
print("\t\t\t\t\t\t\t\tSnake Water Gun Game!!!")
print()
import random
swg = ["s","w","g"]
computer = 0
user = 0
round = 0
name = input("Enter Your Name\n")
while round<10:
    round = round + 1
    print("Round = ", round)
    print("Enter Your Choice ")
    _input = input("'S' for Snake\n'W' for Water\n'G' for Gun\n")
    comp = random.choice(swg)
    if _input == comp:
        print("It's a Tie!!!")
        print("You Both Get 0 Points")
        print(comp)
    elif _input=="s" and comp=="w":
        user = user + 1
        print("You Win This Round!!")
        print(comp)
        print("Your Score is \n", name," = ", user, "Computer = ", computer)
    elif comp=="s" and _input=="w":
        computer = computer + 1
        print("You Loose!!")
        print(comp)
        print("Your Score is \n", name, " = ", user, "Computer = ", computer)
    elif _input=="w" and comp=="g":
        user = user + 1
        print("You Win this Round!!")
        print(comp)
        print("Your Score is \n", name, " = ", user, "Computer = ", computer)
    elif comp=="w" and _input=="g":
        computer = computer + 1
        print("You Loose this Round!!")
        print(comp)
        print("Your Score is \n", name, " = ", user, "Computer = ", computer)
    elif _input=="g" and comp=="s":
        user = user+1
        print("You Win this Round!!")
        print(comp)
        print("Your Score is \n", name, " = ", user, "Computer = ", computer)
    elif comp=="g" and _input=="s":
        computer = computer + 1
        print("You Lose this Round!!ar")
        print(comp)
        print("Your Score is \n", name, " = ", user, "Computer = ", computer)

    else:
        print("Invalid Character!!!")
print()
print("\t\t\t\t\t\t\t\tGame Over!!!")
print()

if user == computer:
    print("This Game is a Ends on a Tie!!")
    print("Your Final Score is \n", name, " = ", user, "Computer = ", computer)
elif user > computer:
    print("Congrats You Won This Game!!!")
    print("Your Final Score is \n", name, " = ", user, "Computer = ", computer)
else:
    print("You Loose this Game!!!\nBetter Luck Next Times..")
    print("Your Final Score is \n", name, " = ", user, "Computer = ", computer)