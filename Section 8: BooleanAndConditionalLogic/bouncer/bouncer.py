# Build a 'bouncer' program. Asks the users age to determine if they need a special wristband to drink etc...

#ask for age
age = input("How old are you?: ")

#Check if user input is an empty string.
if age:
    age = int(age)
    # 18-21 wristband
    if age >= 18 and age < 21:
        print ("You can enter, but need a wristband!")

    # 21+ drink, normal entry
    elif age >= 21:
        print("You are good to enter and can drink!")

    # too young, sorry
    else:
        print("You can't come in little one :(")
else: 
    print("Please enter an age.")