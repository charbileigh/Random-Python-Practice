print("This is a mini list operation project")
print()
print("Ensure that you enter a list with a minimum of 4 entries")
print()
print("For example: [a, b, c, d]")
print()

nums = input("Enter a list of your choice: ")

'''
    This is a mini python project that performs basic list / array operations for any list given.
    All of these operations are manual and stray away from the build-in features.
    This is because, the project aims to help a user identify data structure patterns early on.
'''

# Finds the largest number in a given list
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n
print("\n This is the largest number found in the list: ")


# Finds the smallest number in a given list

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n
print("\n This is the smallest number found in the list: ")


# Sums all the elements within a given list

count = 0

for n in nums:
    count += n
print("\n This is the sum of all the entries in the list: ")

# Counts the number of occurrences of an elements within a list


# Reverses a list
 

# Checks if a list is a palindrome


# Removes duplicates from a list
