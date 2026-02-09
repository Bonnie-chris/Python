# python list -its a build-in data structure that is mutable,ordrerd and uses square brackets
items=['Honda','Mazda','Surf','Volkswagon','Subaru']
#show output
print(items)

# print item at index 2
print(items[2])

# print item at index 3 
print(items[3])

# appending new item 
# append BMW
items.append('BMW')
# show output
print(items)

# inserting items at specific index 
# insert Toyota at index 2
items.insert(2,'Toyota')
# show output
print(items)

# slicing

# 1. slice from index 2 to 5
print(items  [2 : 5])

# 2. print from index 4 and below
print(items [ :4])

# 3. print from index 3 and above 
print(items [3 : ])
