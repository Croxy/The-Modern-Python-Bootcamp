import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1_choice = input("(Enter player1's choice): ")
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
elif computer_choice == 3:
    computer_choice = "scissors"

print("Computer Choice: "+computer_choice)
print("SHOOT!")

if player1_choice and computer_choice:
    if (player1_choice == "paper" or player1_choice == "rock" or player1_choice == "scissors"):
        if player1_choice == computer_choice:
            print("Tie game, play again")
        elif player1_choice == "paper":
            if computer_choice == "rock":
                print("player1 wins!")
            elif computer_choice == "scissors":
                print("player2 wins!")
        elif player1_choice == "rock":
            if computer_choice == "scissors":
                print("player1 wins!")
            elif computer_choice == "paper":
                print("player2 wins!")
        elif player1_choice == "scissors":
            if computer_choice == "paper":
                print("player1 wins!")
            elif computer_choice == "rock":
                print("player2 wins!")
    else:
        print("Each player must select paper, rock, or scissors.")
else:
    print("Each player must input a value, try again!")


