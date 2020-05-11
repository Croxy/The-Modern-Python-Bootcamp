# Add up all odd numbers between 10 and 20

# Solution using a conditional:
# Store the result in x:
x = 0
for num in range(10,21):
    if num % 2 != 0:
        x += num

# Solution using a range step:
# Store the result in x:
x = 0

# The reason this works is that because we know 10 will not be added to the total (as it is odd) we can begin the range at 11.
for i in range(11,21,2):
     x += i