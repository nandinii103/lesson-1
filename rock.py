import random

choices = ["rock" , "paper" , "scissors"]

while True:
    user = input( "Enter rock , paper , or scissors: ")
    computer = random.choice(choices)
    print("The computer chose: " , computer )
    if user== computer:


        print("It is a tie")
    elif user == "rock" and computer == "scissors":
        print("You win")

    elif user == "scissors" and computer == "paper":
        print("You win")

    elif user == "paper" and computer == "rock":
        print("You win")
    else:
        print("computer wins")
    again = input("PLay again?(yes/no)")
    if  again == "no":
        break
    
    