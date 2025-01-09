# The copy() method returns a shallow copy of the list.

# copy() Syntax
new_list = list.copy()


# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()

print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]


""" Ex: 1 Copying a List """
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)

""" Ex: 2 List copy using = """

old_list = [1, 2, 3]

# copy list using =
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)


""" Example: 3 Copy List Using Slicing Syntax """
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)