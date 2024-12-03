"""
Generate two sets – first for all singers and second for all dancers of the class
using set comprehension. Perform set operations to generate the following sets
  a. of all artists of the class
  b. allrounders of the class
  c. dancers but not singers
  d. singers but not dancers
  e. dancers but not singers cum singers but not dancers
"""


# Sample data for singers and dancers in the class
singers = {name for name in ["Alice", "Bob", "Charlie", "David", "Eve"]}
dancers = {name for name in ["Charlie", "David", "Eve", "Frank", "Grace"]}

# a. Set of all artists in the class (Union of singers and dancers)
all_artists = singers | dancers

# b. Set of allrounders in the class (Intersection of singers and dancers)
allrounders = singers & dancers

# c. Set of dancers but not singers (Dancers minus Singers)
dancers_not_singers = dancers - singers

# d. Set of singers but not dancers (Singers minus Dancers)
singers_not_dancers = singers - dancers

# e. Set of dancers but not singers combined with singers but not dancers (Symmetric Difference)
dancers_or_singers_not_both = dancers ^ singers

# Display the results
print("All Artists",all_artists) 
print("All Rounders", allrounders) 
print("Dancers but not singers", dancers_not_singers) 
print("Singers but not dancers", singers_not_dancers), 
print("Dancers or singers not both", dancers_or_singers_not_both)