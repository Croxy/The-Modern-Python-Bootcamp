

# List Comprehension

### What does it do?

It is a shorthand syntax that allows you to generate new lists, make new lists that are direct copies of other lists, or more often than not are tweaked versions. You can take one list and generate a new one that has ever number squared, or every string reversed. It can get more complex than that, but those are simple examples. 

The syntax

```
[ ____ for ____ in ____ ] 

```

```
nums = [1,2,3]

[x*10 for x in nums] # [10,20,30]
```

### List Comprehension vs Looping

You can accomplish the same task with a for loop:

```
numbers = [1,2,3,4,5]

doubled_numbers = []

for num in numbers:
    doubled_number = num *2
    doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2,4,6,8,10]
```

But using list comprehension is much quicker and simpler:

```
numbers = [1,2,3,4,5]
doubled numbers = [num * 2 for num in numbers]
print(doubled_numbers) # [2,4,6,8,10]
```

### Other List Comprehension examples:

Putting each letter in a string into a list and making the letters uppercase.

```
name = 'colt'

[char.upper() for char in name] # ['C', 'O', 'L', 'T']
```

Capitalizing each name in the `friends` list.

```
friends = ['ashley', 'matt', 'michael']
 
[friend.capitalize() for friend in friends]
```


## List Comprehension with Conditional Logic

```
numbers = [1,2,3,4,5,6]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]
```

```
[num*2 if num % 2 == 0 else num/2 for num in numbers]

# [0.5,4,1.5,8,2.5,12]
```

# Nested Lists

Basically, just lists inside of lists. Also called multi-dimensional lists.

```
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
```

```
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

nested_list[0][1] #2

nested_list[1][-1] #6
```

## Printing Values in Nested Lists

To iterate through a nested list you have to use two loops. 

Iterating through nested data structures is a common application for nested loops.

```
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for l in nested_list
    for val in l:
        print(val)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```
## Nested List Comprehension

```
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

[[print(val) for val in l] for l in nested_list]
```

```
board = [[num for num in range(1,3)] for val in range(1,4)]

print(board)

[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]

#[['X','O','X'],['X','O'],['X','O','X']]
```

# Recap

- lists are fundamental data structures for ordered information
- elements in lists can be any type, even other lists.
- We can modify lists using a variety of methods. Append, pop, sort etc...
- slices are quite useful when making copies of lists.
- list comprehension is used everywhere when iterating over lists, strings, ranges, and more data types.
- nested lists are essential for building more complex data structures like matrices, game boards, and mazes.
- swapping is quite useful when shuffling or sorting.
