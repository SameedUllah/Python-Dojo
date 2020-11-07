# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a Dictionary
person = {
    'first_name': 'john',
    'last_name' : 'doe',
    'age' : 30
}

# use a constructor
# person2 = dict(first_name= 'Willam', last_name='smith')

# Get Value
print(person['first_name'])
print(person.get('last_name'))


# Add Key/Value
person['Phone'] = '051-261-248-0'

# Get Keys
print(person.keys())

# Get items
print(person.items())

# Copy dict 
person2 = person.copy()
person2['City'] = 'Boston'
print(person2)

# Remove item
del(person['age'])
person.pop('Phone')

# Clear dict
person.clear()

# Get len
print(len(person2))


# Delete Dict
del(person)

# List of dict
people =  [
    {'name' :'Martha', 'age' : 30},
    {'name': 'kevin' , 'age' : 20}
]

print(people[1]['name'])
