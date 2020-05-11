# Mileage Converter

This is a simple program to learn how to get user input and also put into practice the information learned to this point. This little "project" is focusing on reinforcing the use of variables, strings, data type conversion, and arithmetic operations.

There are two new functions picked up in this project.

First was the `input()` function which changes the prompt in the command line and waits for the user to type something and hit the return/enter key. After input the data will be stored within the assigned variable. 

Second was the `round()` function. This function allows you to specify a float to round and to how many decimal places you would like it to round. 
 > For example  `round(5.123, 1)` would output `5.1`.


```
# Get the kilometer input from the user 
print("How many kilometers did you drive today?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"You said {kms}kms, that is {miles}mi.")
```