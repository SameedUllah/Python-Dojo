# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#  Create a Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Orangees', 'Grapes'))

# Single value needs a trailing comma to be considered as a tuple
fruits2 = ('Apples',)


# get value
print(fruits[0])

# Can't Change Value
# fruits[1] = 'Peach'

# delete tuple
del fruits2

# print(fruits2)

# Get Length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check If in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Add Duplicate
fruits_set.add('Apples')

# Remove from set
# fruits_set.remove('Grapes')

# Clear set
# fruits_set.clear()

# Delete a set
# del fruits_set


print(fruits_set)
