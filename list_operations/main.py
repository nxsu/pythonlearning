# fruits = ['apple','mango', 'peach', 'banana']

# orangeVar = 'orange'

# fruits.append(orangeVar) # this can be a string or var, or any other input that has the value of a listable item.

# print(fruits) 

# print('orange' in fruits) # checks for the string 'orange' in the list fruits. returns a True or False value.

fruits = ['apple', 'mango', 'peach', 'orange']
fruits.append('banana')
fruitslength = len(fruits)
print(len(fruits))
print(fruitslength)
print(fruits)

fruits.insert(1, 'balls')
print(fruits)

print(fruits.index('mango'))

print(fruits)