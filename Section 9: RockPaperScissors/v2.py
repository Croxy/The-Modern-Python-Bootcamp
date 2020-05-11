print("...rock...")
print("...paper...")
print("...scissors...")

player1_choice = input("(Enter player1's choice): ")
player2_choice = input("(Enter player2's choice): ")

print("SHOOT!")

if player1_choice and player2_choice:
    if (player1_choice == "paper" or player1_choice == "rock" or player1_choice == "scissors") and (player2_choice == "paper" or player2_choice == "rock" or player2_choice == "scissors"):
        if player1_choice == player2_choice:
            print("Tie game, play again")
        elif player1_choice == "paper":
            if player2_choice == "rock":
                print("player1 wins!")
            elif player2_choice == "scissors":
                print("player2 wins!")
        elif player1_choice == "rock":
            if player2_choice == "scissors":
                print("player1 wins!")
            elif player2_choice == "paper":
                print("player2 wins!")
        elif player1_choice == "scissors":
            if player2_choice == "paper":
                print("player1 wins!")
            elif player2_choice == "rock":
                print("player2 wins!")
    else:
        print("Each player must select paper, rock, or scissors.")
else:
    print("Each player must input a value, try again!")