# The append() method adds an item to the end of the list.
# Syntax of List append()
# list.append(item)
# item - an item (number, string, list etc.) to be added at the end of the list

currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')

print(currencies)

""" Example 1: Adding Element to a List """
# animals list
animals = ['cat', 'dog', 'rabbit']

# Add 'guinea pig' to the list
animals.append('guinea pig')

print('Updated animals list: ', animals)


""" Example 2: Adding List to a List """
# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to animals
animals.append(wild_animals)
wild_animals.append(animals)

print('Updated animals list: ', animals)
print('Updated animals list: ', wild_animals)



