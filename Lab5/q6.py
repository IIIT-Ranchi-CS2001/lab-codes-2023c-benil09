"""
WAP to count the number of each character present in a string using the
concept of a dictionary.
"""


string = input("Enter a string: ")

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1  

# Print the character counts
print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")