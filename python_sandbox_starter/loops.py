# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'paul','sara','william']

# for loop
# for person in people:
#     if person == 'sara':
#         print(f'Reaached @ {person}')
#         break
#     print(F'Current Person {person}')

# Break
# for person in people:
#     if person == 'sara':
#         break
#     print(F'Current Person {person}')

# Continue
# for person in people:
#     if person == 'sara':
#         continue
#     print(F'Current Person {person}')

# Range
# for i in range(len(people)):
#     print(people[i])

# for i in range (0,11):
#     print(f'the number is {i}')

# While loops execute a set of statements as long as a condition is true.

# count = 0
# while count <=10:
#     print(f'Count {count}')
#     count +=1


sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print (sheep.count(True))
# def count_sheeps (sheep):


# present = 0
# missing = 0

# for i in sheep:
#     if i == True :
#         present += 1
#     else :
#         missing += 1

# print(f'There are {present} sheeps in total, not {present + missing}')




# string = "This website is for losers LOL!"
# vovel = ['a','e','i','o','u','O']
# for i in string:
#     # print(i)
#     if i ==  vovel:
#         continue 
#     print(i)