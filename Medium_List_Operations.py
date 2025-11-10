import ast

print("This is a mini list operation project")
print()
print("Ensure that you enter the first and second list of your choice with a minimum of 4 entries")
print()
print("For example: [a, b, c, d]")
print()


'''
    This is a mini python project that performs medium list / array operations for any list given.
    All of these operations are manual and stray away from the build-in features.
    This is because, the project aims to help a user identify data structure patterns early on.
'''

# inputting the list of the user's choice
# List example used for testing purposes: [3, 7, 2, 9, 5, 5, 5]
nums1 = input("Enter the first list of your choice (like [3,7,2]) : ")
nums1 = ast.literal_eval(nums1)

# inputting the list of the user's second choice
# Second list example: [2, 6, 2, 9, 6, 7, 5]
nums2 = input("\n Enter the second list of your choice (like [3,7,2]) : ")
nums2 = ast.literal_eval(nums2)

target = input("\n Enter the target to be used in the two sorted array question: ")
target = int(target)

print("\n -----------------------------------  Answers using the lists and target  ------------------------------------")

# Validate a mountain array for nums1 
def is_mountain(nums1):
    n = len(nums1)
    if n < 3: 
        return "\n This list is not a mountain array"

    i = 0
    # climb up
    while i + 1 < n and nums1[i] < nums1[i + 1]:
        i += 1

    # peak cannot be first or last
    if i == 0 or i == n - 1:
        return "\n This list is not a mountain array"

    # climb down
    while i + 1 < n and nums1[i] > nums1[i + 1]:
        i += 1

    return "\n This list is a mountain array"
print(is_mountain(nums1))


# Validate a mountain array for nums2
def is_mountain(nums2):
    
    n = len(nums2)
    if n < 3: 
        return False

    i = 0
    # climb up
    while i + 1 < n and nums2[i] < nums2[i + 1]:
        i += 1

    # peak cannot be first or last
    if i == 0 or i == n - 1:
        return False

    # climb down
    while i + 1 < n and nums2[i] > nums2[i + 1]:
        i += 1

    return "\n This list is a mountain array"
print(is_mountain(nums2))

# Two sum in a sorted array for nums1
def two_sum_sorted(nums1, target):
    left = 0
    right = len(nums1) - 1

    while left < right:
        s = nums1[left] + nums1[right]
        if s == target:
            return (left, right)
        if s < target:
            left += 1
        else:
            right -= 1
    return None

print("\n This is the two sum in the first sorted array: ", two_sum_sorted(nums1, target))


# Two sum in a sorted array for nums2
def two_sum_sorted(nums2, target):
    left = 0
    right = len(nums2) - 1

    while left < right:
        s = nums2[left] + nums2[right]
        if s == target:
            return (left, right)
        if s < target:
            left += 1
        else:
            right -= 1
    return None

print("\n This is the two sum in the second sorted array: ", two_sum_sorted(nums2, target))