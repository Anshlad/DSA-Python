# The list's sort() method sorts the elements of a list.

# sort() Syntax
# numbers.sort(reverse, key)

# The sort() method can take two optional keyword arguments:
# reverse - By default False. If True is passed, the list is sorted in descending order.
# key - Comparion is based on this function.


# prime_numbers = [11, 3, 7, 5, 2]

# # sort the list in ascending order
# prime_numbers.sort()

# print(prime_numbers)

# Output: [2, 3, 5, 7, 11]

""" Ex: 1 Sort in Descending order """
# numbers = [7, 3, 11, 2, 5]

# # reverse is set to True
# numbers.sort(reverse = True)

# print(numbers)

"""" Ex: 2 Sort a List of Strings """
# cities = ["Tokyo", "London", "Washington D.C"]

# sort in dictionary order
# cities.sort()
# print(f"Dictionary order: {cities}")
# print(cities)

# sort in reverse dictionary order
# cities.sort(reverse = True)
# print(f"Reverse dictionary order: {cities}")

""" Ex: 3 Reverse Strings Based on Length """
text = ["abc", "wxyz", "gh", "a"]

# stort strings based on their length
text.sort(key = len)
print(text)

