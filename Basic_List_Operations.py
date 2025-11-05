import ast

print("This is a mini list operation project")
print()
print("Ensure that you enter a list with a minimum of 4 entries")
print()
print("For example: [a, b, c, d]")
print()


'''
    This is a mini python project that performs basic list / array operations for any list given.
    All of these operations are manual and stray away from the build-in features.
    This is because, the project aims to help a user identify data structure patterns early on.
'''
# inputting the list of the user's choice
 
nums = input("Enter a list of your choice (like [3,7,2]) : ")
nums = ast.literal_eval(nums)

# Finds the largest number in a given list
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n
print("\n This is the largest number found in the list: ", largest)


# Finds the smallest number in a given list

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n
print("\n This is the smallest number found in the list: ", smallest)


# Sums all the elements within a given list

count = 0

for n in nums:
    count += n
print("\n This is the sum of all the entries in the list: ", count)


# Counts the number of occurrences of an elements within a list
print()
occur = 0
target = input("Enter the element you want to check occurs in the list: ")
target = int(target)

for n in nums:
    if n == target:
        occur += 1
print("\n The chosen target appears in the given list, this many times: ", occur)

# Reverses a list
left = 0
right = len(nums) - 1

while right > left:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
print("\n This is the reversed list: ", nums)
 
# Checks if a list is a palindrome
left = 0
right = len(nums) - 1
palindrome = True

for n in nums:
    if nums[left] != nums[right]:
        palindrome = False
        break
    left += 1
    right -= 1

if palindrome == True:
    print("\n This list is a palindrome")
else:
    print("\n This list is not a palindrome")

# Removes duplicates from a list
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)
print("\n This is the updated list without duplicates: ", unique)