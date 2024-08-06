# Define a sample string
sample_string = "Hello, World!"

# Print the original string
print("Original string:", sample_string)

# String length
print("Length of string:", len(sample_string))

# Accessing individual characters
print("First character:", sample_string[0])
print("Last character:", sample_string[-1])

# String slicing
print("Substring from index 1 to 5:", sample_string[1:6])

# Reversing a string
reversed_string = sample_string[::-1]
print("Reversed string:", reversed_string)

# Counting occurrences of a character
char_count = sample_string.count('l')
print("Occurrences of 'l':", char_count)

# Checking if a string starts/ends with a specific substring
print("Starts with 'Hello':", sample_string.startswith("Hello"))
print("Ends with 'World!':", sample_string.endswith("World!"))

# Converting to uppercase and lowercase
print("Uppercase:", sample_string.upper())
print("Lowercase:", sample_string.lower())

# Finding the index of a substring
substr_index = sample_string.find("World")
print("Index of 'World':", substr_index)

# Replacing substrings
new_string = sample_string.replace("Hello", "Hi")
print("After replacement:", new_string)

# Splitting a string into a list
split_list = sample_string.split(", ")
print("Split list:", split_list)
