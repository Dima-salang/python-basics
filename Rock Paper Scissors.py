import random
data = input("Your move: ")
move = random.choice(range(3))
rock = "Rock"
scissors = "Scissors"
paper = "Paper"

if move == 0:
    print(rock)
    if rock == data:
        print("It's a draw!")
    elif data == paper:
        print("You win!")
    elif data == scissors:
        print("You lost!")
if move == 1:
    print(scissors)
    if scissors == data:
        print("It's a draw!")
    elif data == paper:
        print("You lost!")
    elif data == rock:
        print("You win!")
if move == 2:
    print(paper)
    if paper == data:
        print("It's a draw!")
    elif data == rock:
        print("You lost!")
    elif data == scissors:
        print("You win!")




