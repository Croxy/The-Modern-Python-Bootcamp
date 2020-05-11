# Loop through numbers 1-20 (inclusive)
# for 4 and 13, print "x is unlucky"
# for even numbers, print "X is even"
# for odd numbers, print "x is odd"

for num in range(1, 21):
    if num % 2 == 0:
        if num == 4:
            print(f"{num} is UNLUCKY!")
        else:
            print(f"{num} is even")
    elif num % 2 != 0:
        if num == 13:
            print(f"{num} is UNLUCKY!")
        else:
            print(f"{num} is odd")