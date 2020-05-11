# Get the kilometer input from the user 
print("How many kilometers did you drive today?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"You said {kms}kms, that is {miles}mi.")