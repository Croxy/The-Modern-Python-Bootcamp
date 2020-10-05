import random

player_wins = 0

comp_wins = 0

while player_wins < 2 and comp_wins < 2:
    print (f"Player 1 Score: {player_wins}")
    print (f"Computer Score: {comp_wins}")
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
                    player_wins += 1
                elif computer_choice == "scissors":
                    print("computer wins!")
                    comp_wins += 1
            elif player1_choice == "rock":
                if computer_choice == "scissors":
                    print("player1 wins!")
                    player_wins += 1
                elif computer_choice == "paper":
                    print("computer wins!")
                    comp_wins += 1
            elif player1_choice == "scissors":
                if computer_choice == "paper":
                    print("player1 wins!")
                    player_wins += 1
                elif computer_choice == "rock":
                    print("computer wins!")
                    comp_wins += 1
        else:
            print("Each player must select paper, rock, or scissors.")
    else:
        print("Each player must input a value, try again!")

print("***Final Score***")
print (f"Player 1 Score: {player_wins}")
print (f"Computer Score: {comp_wins}")

if player_wins > comp_wins:
    print("Player wins!")
else:
    print("Computer wins!")
