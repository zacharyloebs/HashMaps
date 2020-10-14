# This program demonstrates how the HashMap (Dictionary) data structure works in Python

# O(n) complexity
# Space O(n)
# Get Item O(1)
# Set Item O(1)
# Delete Item O(1)
# Iterate O(n)

# Hash maps store key-value pairs
my_dict = {
    1: "green",
    2: "purple",
    3: "orange",
    4: "gray",
    5: "blue"
}

# Print the contents of the hashmap
print(my_dict)

# Find the length (number of pairs) of the hashmap
print(len(my_dict))

# Access specific elements of a hash map
# Prints the value corresponding with the key
print(my_dict[1])

# Change the value of a specific key
my_dict[3] = "yellow"
# Value of key "3" has been changed
print(my_dict[3])

# Add a key-value pair to the hashmap
my_dict[6] = "red"
# New key-value has been added
print(my_dict)

# Removes the last key-value pair from the hashmap
my_dict.popitem()
# Last key-value pair has been removed
print(my_dict)

# Removes a specific key-value pair from the hashmap
del my_dict[5]
# Key-value pair with the key of "5" has been removed
print(my_dict)
