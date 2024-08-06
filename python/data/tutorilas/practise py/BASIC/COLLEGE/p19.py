# Define a sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the original list
print("Original list:", sample_list)

# Slicing the list
# Syntax: list[start_index:end_index:step]
# If start_index is not provided, it defaults to 0
# If end_index is not provided, it defaults to the end of the list
# If step is not provided, it defaults to 1

# Extracting elements from index 2 to 5 (exclusive)
sliced_list1 = sample_list[2:5]
print("Sliced list 1:", sliced_list1)

# Extracting elements from index 0 to 7 (exclusive) with a step of 2
sliced_list2 = sample_list[0:7:2]
print("Sliced list 2:", sliced_list2)

# Extracting elements from index 3 to the end of the list
sliced_list3 = sample_list[3:]
print("Sliced list 3:", sliced_list3)

# Extracting elements from the beginning to index 5 (exclusive)
sliced_list4 = sample_list[:5]
print("Sliced list 4:", sliced_list4)

# Reversing the list using slicing
reversed_list = sample_list[::-1]
print("Reversed list:", reversed_list)
