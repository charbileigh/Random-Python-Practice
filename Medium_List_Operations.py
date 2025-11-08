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