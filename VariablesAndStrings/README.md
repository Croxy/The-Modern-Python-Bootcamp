# Section 7: Variables and Strings

In this section I am introduced to concepts surrounding variables and strings.

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
    * String Concatenation
        * Concatenation is combining multiple strings together. In Python you can do this with the "+" operator.

        ```
        str_one = "your"
        str_two = "face"
        str_three = str_one + " " + str_two # your face
        ```

        * You can also use the "+=" operator

        ```
        str_one = "ice"
        str_one += " cream"
        str_one # ice cream
        ```
    * Formatting Strings
        * There are also several ways to format strings in Python to **interpolate** variables. 
            * F-Strings

                ```
                x = 10
                formatted = f"I've told you {x} times already!"
                ```
    * Referencing characters in a string
        * From beginning
        ```
        name = "Ryan"
        print(name[0]) # R
        ```

        * From end
        ```
        name = "Ryan"
        print(name[-1]) # n
        ```

- Learn how to convert data types (int to string, string to int, int to float etc...)
    * In string interpolation, data types are implicitly converted into string form (more on this later in OOP)
    * You can also explicitly convert variables by using the name of the builtin type as a function (more on functions later)
    ```
    decimal = 12.1234567
    integer = int(decimal) # 12 (this doesn't round)
    ```

    ```
    my_list = [1, 2, 3]
    my_list_as_a_string = str(my_list) # "[1, 2, 3]"
    ```

- Build a silly program that gest user input.

    * How to get user input
        * the `input()` function changes the prompt in the command line and waits for the user to type something and hit the return/enter key.
    ```
    #Get the kilometer input from the user 
    print("How many kilometers did you drive today?")
    kms = input()
    print(f"You said {kms} kilometers")
    ```

