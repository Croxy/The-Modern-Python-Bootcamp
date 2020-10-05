# LISTS

- What is a list?

It is just a collection or grouping of items. Those items could be anything really (strings, booleans, other lists etc...) Basically, it is a way to combine data into one variable that has a data structure.

# Objectives

- Describe, create, and access a list data structure
- Use built in methods to modify and copy lists
- Iterate over lists using loops and list comprehensions
- Work with nested lists to build more complex data structures

# Creating Lists

- How are Lists useful?

A fundamental data structure for organizing collections of items. 

A list looks like this:

```
tasks = ["Install Python", "Learn Python", "Take a break"]
```

A list can also be created using variables.

```
first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"

tasks = [first_task,second_task,third_task]
```

#Built-in Functions

Get the length of items: ```len(list)```

Another way to build a list:

```
r = range(1,10)
list(r)
```

This builds a list of numbers.

# Accessing Values in a List

```
friends = ["Ashley", "Matt", "Michael"]
```

Like ranges, lists always start counting at zero. So the first element lives at index 0. 

For example, ```friends[0]``` is "Ashley.

You can print the list value using the print command.

```
print(friends[0]) # 'Ashley'
```

## Accessing Values from the end

You can use a negative number to index backwards.

```
print(friends[-1]) # 'Michael'
print(friends[-3]) # 'Ashley'
print(friends[-4]) # Index Error
```

# Check if a Value is in a list

```
"Ashley" in friends # True

"Colt" in friends # False
```

# Accessing All Values in a List

You could print each item one at a time, but that would require more lines of code than needed and it doesn't scale with larger lists.

The solution would be to use a `for` or `while` loop.

```
numbers = [1,2,3,4]

for number in numbers:
    print(number)
```

```
numbers = [1,2,3,4]
i=0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

# List Methods

Working with lists is very common, and there are quite a few things that you can do with them.

## Functions vs Methods

Built-in functions (`print()`, `len` etc...) can be used on any type of variable. 

Methods are associated to a specific to a variable type. In the following cases, these are list methods.

### append

Adds an item to the end of a list.

```
first_list = [1,2,3,4]
first_list.append(5)
print(first_list) # [1,2,3,4,5]
```

> append only allows one argument, e.g. `first_list.append(5,7)` fails.

### extend

Add to the end of a list all values passed to the `extend` method.

```
correct_list = [1,2,3,4]
correct_list.extend([5,6,7,8])
print(correct_list) # [1,2,3,4,5,6,7,8]
```

### insert

Insert an item at a given position.

```
first_list = [1,2,3,4]
first_list.insert(2, 'Hi!')
print(first_list) # [1,2, 'Hi!',3,4]
first_list.insert(-1, 'The end!')
print(first_list) # [1,2, 'Hi!',3,'The end!',4]
```


### clear

Remove all items from the list.

```
first_list = [1,2,3,4]
first_list.clear()
print(first_list) # []
```

### pop

Remove an item at the given position in the list and return it.

If no index is specificed pop will remove and return the last item in the list.

```
first_list = [1,2,3,4]
first_list.pop() # 4
first_list.pop(1) # 2
```

### remove

Remove the first item from the list whose value is `x`. 

Throws a ValueError if the item is not found.

```
first_list = [1,2,3,4,4,4]
first_list.remove(2)
print(first_list) # [1,3,4,4,4]
first_list.remove(4)
print(first_list) # [1,3,4,4]
```

### index

Find the index or position of a given item within a list.

```
numbers = [5,6,7,8,9,10]
numbers.index(6) # 1
numbers.index(9) # 4
```

Can specify start and end

```
numbers = [5,5,6,7,5,8,8,9,10]

numbers.index(5) #0
numbers.index(5,1) #1
numbers.index(5,2) #4

numbers.index(8,6,8) #6
```

### count

Ouputs the number of times that the input appears in the list.


```
numbers = [1,2,3,4,3,2,1,4,10,2]

numbers.count(2) # 3
numbers.count(21) # 0
numbers.count(3) # 2
```

### reverse

Revers the elements of the list (in-place).

```
first_list = [1,2,3,4]

first_list.reverse()

print(first_list) # [4,3,2,1]
```

### sort

Sort the items of the list (in-place).

```
another_list = [6,4,1,2,5]
another_list.sort()
print(another_list) # [1,2,4,5,6]
```

### join


- Technically is a _string method_ that takes an iterable argument. 

- Commonly used to convert lists to strings.

- It concatenates a copy of the base string _between_ each item of the iterable.

- returns a new string

- can be used to make sentences out of a list of words by joining on a space, for instance:

```
words = ["Coding", "Is", "Fun"]

' '.join(words) # Coding Is Fun
```

```
name = ["Mr", "Steele"]
'. '.join(name) # Mr. Steele
```



