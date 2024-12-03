"""
Write a python script using map, lambda and filter functions to do the following
operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22
2@$”


To find all the letters given in the string and to convert them to uppercase
 o/p: [‘TOM’]
 
To find all the digits present in the string and to find their squares
 o/p: [625]
 
To display all the alphanumeric characters present in the string
  o/p: [“Tom”,‘25’,“Rahu22”]


"""


# Input a comma-separated string
input_string = input("Enter a comma-separated string: ")

# Split the input string into a list of substrings
substrings = input_string.split(' ')

# Operation 1: Find all letters and convert to uppercase
letters_uppercase = list(
    map(
        lambda s: s.upper(),
        filter(lambda s: s.isalpha(), substrings)
    )
)

# Operation 2: Find all digits and compute their squares
digits_squared = list(
    map(
        lambda s: int(s) ** 2,
        filter(lambda s: s.isdigit(), substrings)
    )
)

# Operation 3: Display all alphanumeric strings
alphanumeric = list(
    filter(lambda s: s.isalnum(), substrings)
)

# Output the results
print("Uppercase letters:", letters_uppercase)
print("Squares of digits:", digits_squared)
print("Alphanumeric characters:", alphanumeric)