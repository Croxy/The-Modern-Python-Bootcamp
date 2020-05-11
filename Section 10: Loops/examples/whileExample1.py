
# Use a while loop to check user input matches a specific value.
msg = input("what is the secret password?")

while msg != "bananas":
    print("WRONG!")
    msg = input("what is the secret password?")
print("CORRECT!")

# Use a while loop to create for loop functionality.
num = 1

while num < 11:
    print(num)
    num += 1
    