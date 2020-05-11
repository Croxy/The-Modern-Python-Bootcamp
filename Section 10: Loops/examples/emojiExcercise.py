# print emojis in a pyramid pattern using a while AND for loop.

# solution using a for loop
for i in range (10):
        print("\U0001f600"*(i+1))

# solution using a while loop
num = 1
while num <= 10:
    print("\U0001f600"*(num))
    num += 1

#nested solution without string multiplication
for num in range (1,11):
    count = 1
    smileys = "\U0001f600"
    while count < num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)
