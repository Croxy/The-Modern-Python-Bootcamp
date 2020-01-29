# Ints and Floats

Python has two main ways to represent numbers. 

|Integer|Float|
 |--|--|
 |4|6.1|
 |57|1.3333|
 |-10|0.0|

Integers typically take up less space in memory.  
 
This is because when storing floats/decimals Python has to account for an infinite number of decimal points that could come after.  

There are also "complex" and "long" data types, but the use cases are rare. 


# Numbers and Math

Python Math Operators 

|Symbol|Name|
|--|--|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|**|Exponentiation|
|%|Modulo|
|//|Integer Division|

In Python division always returns a float. 

Python follows the order of operations (PEMDAS). 

print(2 ** 3) #"**" indicates an exponent. 

print(49 ** 0.5) #Square root of 49 

print(10 % 3) #Modulo, kind of like division. AKA: The remainder operator. 

print(10//3) # // integer division, does the division, just returns an int. Always rounds down. 
 
> **NOTE**: '# ' is the comment character. 

> **NOTE**: Python 3 Documentation URL: https://docs.python.org/3/ 

# Variables and Data Types

- Understand how to assign and use variables
    * A variable in Python is like a variable in mathematics: it is a named symbol that holds a value.
    * Variables in Python are always assigned with the variable name on the left and the value on the right of the equals sign.
    * Variables must be assigned _before_ they can be used.
    ```
    x = 100 
    khaleesi_mother_of_dragons = 1
    print(khaleesi_mother_of_dragons + x)
    101    
    ```
    * Variables can be:
        * Assigned to other variables
        * Reassigned at any time
        * assigned at the same time as other variables.

        ```
        python_is_awesome = 100
        just_another_var = python_is_awesome
        python_is_awesome = 1337
        all, at, once = 5, 10, 15
        ```

- Learn Python variable naming restrictions and conventions
    * Naming Restrictions
        * Variables have to start with a letter or underscore
        * The rest of the name must consist of letters, numbers, or underscores
        * Names are case-sensitive
    * Naming Conventions/Style
        * Most variables should be snake_case (underscores between words)
        * Most variables should also be lowercase, with some exceptions.
            * CAPITAL_SNAKE_CASE usually refers to constants. (e.g. PI = 3.14)
            * UpperCamelCase usually refers to functions.
            * Variables that start and end with two underscores are called "dunders" (dunder for double underscore) are supposed to be private or left alone. `__this_is_a_dunder__`
        
- Learn some of the different data types available in Python
    * When a variable is assigned, it must be a valid data type.
    * Most common data types used in Python:

    |Data Type|Description|
    |--|--|
    |bool|True or False values, case sensitive, must be capital T or F to work as a boolean.|
    |int| an integer (1,2,3)|
    |str|(string) a sequence of Unicode characters inside quotes, e.g. "Colt", "Ryan", "2"|
    |list|an ordered sequence of values of other data types, e.g. [1,2,3] or ["a","b","c"]|
    |dict|a collection of key:value pairs e.g. {"first_name":"Ryan", "last_name":"Cox"}|

    > Special Value: `None` - value Python uses to represent the idea of nothingness, or a "null" variable. Similar to `True` and `False` this value must be capitalized for Python to treat the variable assigned as "null". 

- Learn why Python is called a dynamically typed language
    * Python is highly flexible about reassigning variables to different types:
        ```
            awesomeness = True
            print(awesomeness) # True

            awesomeness = "a dog" 
            print(awesomeness) # a dog

            awesomeness = None
            print(awesomeness) # None

            awesomeness = 22/7
            print(awesomeness) # 3.142857...
        ```
    * Because Python allows variables to change data types readily it is considered a Dynamically Typed language.
    * Other languages are statically typed (like C++) and require variables to be stuck with their originally assigned data types.


- Learn how to convert data types (int to string, string to int, int to float etc...)
- Learn the ins and outs of Strings!
    * Declaring strings
        * String literals in Python can be declared with either single or double quotes.
        ```
            my_string = 'a hat'
            this_other_string = "a cat"
        ```
        * While either is fine, you should stick to the same convention through a file and/or project. Being consistent is good practice.

    > A note on Using quotes inside quotes: You can use single quotes inside double quotes, or double quotes inside of single quotes. You can never use single inside single, or double inside double.

    * Using [escape characters (sequences?)](https://docs.python.org/3/reference/lexical_analysis.html)
        * In Python there are also "escape characters" (most languages support these), which are "metacharacters" - they get interpreted by Python to do something special. 
        * A few of these characters that would be good to note before moving forward:
            > All escape characters start with a '\\' (backslash).
            * `\n` - Creates a new line in a variable.
            * `\"`, `\'` - Allows for printing double and single quotes inside of other double or single quotes.

- Build a silly program that gest user input.

