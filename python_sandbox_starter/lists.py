# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5,6]

fruits = ['Appels', 'Oranges', 'Mangoes', 'Bananas']

# Use a Constructor
# numbers1 = list((1,2,3,4,5,6))

# Get Length
print(len(fruits))

# Get a value
print(fruits[0])

# Append to list
fruits.append('Grapes')

# Change Values
fruits[0] = 'Blueberries'

# Remove from list
fruits.remove('Grapes')

# Insert to position
fruits.insert(2, 'Straberries')

# Remove with pop
fruits.pop(2)

# Reverse List
fruits.reverse()

# Sort list
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)