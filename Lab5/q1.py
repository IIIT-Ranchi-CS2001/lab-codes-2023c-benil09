"""
Generate two tuples to represent two distinct points in space. (Three
dimensional geometry). Determine the Euclidean distance between the two.
"""

import math

point1 = (3, 4, 5)
point2 = (7, 1, 9)


distance = math.sqrt((point2[0] - point1[0])**2 + 
                     (point2[1] - point1[1])**2 + 
                     (point2[2] - point1[2])**2)

# Display the points and the calculated distance
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Euclidean Distance: {distance:.2f}")