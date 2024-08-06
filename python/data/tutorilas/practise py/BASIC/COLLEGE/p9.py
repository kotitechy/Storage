import re

def validate_text(text):
    # Regular expression pattern to match a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the text matches the pattern
    if re.match(pattern, text):
        return True
    else:
        return False

# Test the function
text_to_validate = input("Enter the text to validate: ")
if validate_text(text_to_validate):
    print("Valid text!")
else:
    print("Invalid text!")
