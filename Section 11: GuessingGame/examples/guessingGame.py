import random

user_input = None

computer_num = random.randint(1,10)

while user_input != computer_num:
    user_input = int(input("guess a number between 1 and 10: "))
    if user_input > 0 or user_input < 11:
        if user_input > computer_num:
            print("Too high, try again!")
        elif user_input < computer_num:
            print("Too low, try again!")
        elif user_input == computer_num:
            print("You guessed it! You won!")
            play_again = input("Would you like to play again? (y/n): ")
            if play_again == "y":
                user_input = None
                computer_num = random.randint(1,10)
            else: 
                break
