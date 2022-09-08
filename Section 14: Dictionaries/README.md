# Dictionaries

## Objectives

- Describe, create and access a dictionary data structure.
- Use built in methods to modify and copy dictionaries.
- Iterate over dictionaries using loops and dictionary comprehensions.
- Compare and contrast dictionaries and lists.

## Limitations of Lists

Lists do not provide any information about _what_ an item is.

Dictionaries provide the ability to model data in a way that describes what the items within _are_.

A dictionary is a data structure that consists of key-value pairs.

We use the keys to describe our data and the values to represent the data.

## Dictionary Example

```
instructor = {
    "name" : "Colt",
    "owns_cat" : True, #R.I.P dog :(
    "num_courses" : 4,
    "favorite_language" : "Python",
    "is_hilarious" : True,
    44 : "my favorite number"
}
```

Dictionaries are always key-value pairs. Keys and values separated by colon. Keys are almost always numbers or strings.

### Another way to create a dictionary

Another approach is to use the `dict` function. 

You assign values to keys by passing in keys and values sepertaed by an `=` sign.

```
another_dictionary = dict(key = 'value)
another_dictionary # {'key' : value}
```
## Accessing Individual Values

```
instructor = {
    "name" : "Colt",
    "owns_cat" : True, #R.I.P dog
    "num_courses" : 4,
    "favorite_language" : "Python",
    "is_hilarious" : True,
    44 : "my favorite number"
}

instructor["name"] # "Colt"
instructor["thing"] # KeyError
```

## Accessing All Values or All Keys

To access all values in a dictionary you need to iterate over it.

To get values you need to use `.values()`.

To get keys you need to use `.keys()`.

```
instructor = {
    "name" : "Colt",
    "owns_cat" : True, #R.I.P dog
    "num_courses" : 4,
    "favorite_language" : "Python",
    "is_hilarious" : True,
    44 : "my favorite number"
}

# accessing all values
for value in instructor.values():
    print(value)

# "Colt"
# True
# 4
# 'Python'
# False
# 'my favorite number

# accessing all keys
for key in instructor.keys():
    print(key)

# name
# owns_cat
# num_courses
# favorite_language
# is_hilarious
# 44

```

## Accessing All Keys and Values

using `.items()`

```
for key,value in instructor.items():
    print(key,value)

# name "Colt"
# owns_cat True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number"
```
## Testing for the existence of keys or values

Does a dictionary have a key?

```
"name" in instructor #True
"awesome" in instructor #False
```

Does a dictionary have a value?

```
"Colt" in instructor.values() #True
"Nope" in instructor.values() #False
```

## Dictionary Methods

`.clear()` - Clears all the keys and values in a dictionary.

```
d = dict(a=1,b=2,c=3)
d.clear()
d # {}
```

`.copy()` - Makes a copy of a dictionary.

```
d = dict(a=1,b=2,c=3)
c = d.copy()
c #{'a':1,'b':2,'c':3}
c is d #False
```

`.fromkeys()` - Creates key-value pairs from comma separated values. Usually used to create dictionaries with default values.

```
{}.fromkeys("a","b") # {'a' : 'b'}
{}.fromkeys(["email], 'unknown) #{'email': 'unknown}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1,2,3,4,5]}
```
`.get()` - Retrieves a key in an object and return None instead of a Keyrorr if the key does not exist.

```
d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1

d['b'] # 2
d.get('b') # 2

d['no_key'] # KeyError
d.get('no_key') # None
```

`.pop()` - Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.

```
d = dict(a=1,b=2,c=3)
d.pop() #TypeError: pop expected at least 1 arguments got 0
d.pop('a') # 1
d # {'c':3,'b':2}
d.pop('e') # KeyError
```

`.popitem()` - removes a random key in a dictionary.

`.update` - Update keys and values in a dictionary with another set of key value pairs. 

```
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite and existing key

second['a'] = "AMAZING"

# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
second # # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

## Data Modeling


Modeling a music playlist

```
playlist = {
    'playlist_title': 'My Playlist',
    'playlist_creator': 'Ryan Cox',
    'songs': [
        {'title': 'Happiness Is A Warm Gun', 'artists': ['The Beatles'], 'album': 'The White Album', 'release_date': '1968-11-22', 'song_duration': 2.73},
        {'title': 'Everlong', 'artists': ['Foo Fighters'], 'album': 'The Colour and the Shape', 'release_date': '1997-05-20', 'song_duration': 2.73},
        {'title': 'Be Afraid', 'artists': ['Jason Isbell', 'The 400 Unit'], 'album': 'Reunions', 'release_date': '2020-05-15', 'song_duration': 2.73}
    ]
}
```

## Dictionary Comprehension


```{___:___ for ___ in ___}```

- iterates over keys by default
- to iterate over keys and values use .items()

```
numbers = dict(first=1, second=2, third= 3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
```

You can also create a dictionary from a list by iterating over it with a comprehension:

```
{num: num**2 for num in [1,2,3,4,5,]} # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```
str1 = "ABC"
str2 = "123"
combo = {str[i]: str2[i] for i in range(0,len(str1))}
print combo # # {'A': '1', 'B': '2', 'C': '3'}
```

### Conditional Logic With Dictionaries

```
num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd) for num in num_list }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

```

