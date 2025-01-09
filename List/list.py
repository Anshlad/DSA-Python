# 1. Lists are ordered collection of data items
# 2. They store multiple items in a single variable
# 3. List items are separated by commas and enclosed within square brackets
# 4. Lists are changable meaning we can alter them after creation.


# Example 1
# l = [10, 20, 30]
# l1 = [20, 30, 40]

# print(l)
# print(l1)
# print(type(l))
# l2 = ["Bhavesh", "Nitesh", "Ram"]
# print(l2)
# l3 = [1, 2, "Bhavesh"]
# print(l3)


# Example 2
# marks = [10, 20, 30]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# Example 3
# marks = [10, 20, 30, "Bhavesh", False]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])


# Example 4 - Negative Indexing
# marks = [10, 20, 30, "Bhavesh", False]
# print(marks[-3]) #Negative Index
# print(marks[len(marks)-3]) #Positive Index
# print(marks[5-3]) #Positive Index
# print(marks[2]) #Positive Index

# Check Whether an Item is present in the list?
# marks = [10, 20, 30, "Bhavesh", False]
# if 30 in marks:
#     print("Yes")
# else:
#     print("No")

# Access the value
marks = [10, 20, 30, "Bhavesh", False]
print(marks)
# : slice operator
print(marks[:]) 
print(marks[1:])


