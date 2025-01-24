# Creating and printing a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing a dictionary value using a key
print(thisdict["brand"])

# Demonstrating that duplicate keys are not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020  # This will overwrite the previous value of "year"
}
print(thisdict)

# Getting the number of items in a dictionary
print(len(thisdict))

# Dictionary items can contain various data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Checking the type of a dictionary
print(type(thisdict))

# Using the dict() constructor to create a dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# 1. Using pop() method - removes the item with the specified key name
thisdict.pop("model")
print(thisdict)  # Output: {'brand': 'Ford', 'year': 1964}

# 2. Using popitem() method - removes the last inserted item
# In Python versions before 3.7, popitem() would remove a random item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang'}

# 3. Using del keyword - removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)  # Output: {'brand': 'Ford', 'year': 1964}

# 4. Using del keyword - can delete the dictionary completely
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)  # Uncommenting this will cause an error because "thisdict" no longer exists

# 5. Using clear() method - empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)  # Output: {}

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

