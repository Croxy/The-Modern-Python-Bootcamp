# Loop through numbers 1-20 (inclusive)
# for 4 and 13, print "x is unlucky"
# for even numbers, print "X is even"
# for odd numbers, print "x is odd"

for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    elif num % 2 != 0:
        state = "odd"
    
    print(f"{num} is {state}")