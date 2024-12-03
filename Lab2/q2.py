"""
2. For the given string S=”Ba Ba Black Sheep” , determine the following using built in functions:
      a. The length of the string S
      b. The first occurrence of the letter ‘e’
      c. The total number of occurrences of ‘a’
      d. Generate “Ta Ta Black Sheep”
"""

S="Ba Ba Black Sheep"

# a. The length of the string S
a=len(S)
print(a)

# b. The first occurance of letter 'e'

b=S.find('e')
print(b)

c=S.count('a')
print(c)

d=S.replace("Ba","Ta")
print(d)
    
