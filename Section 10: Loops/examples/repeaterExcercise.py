# Create a simple program to repeat a print statement based on user input.

user_input = int(input("How many times do I have to tell you?"))

if user_input:
    for num in range(user_input):
        print(f"time {num+1}: CLEAN YOUR ROOM!")