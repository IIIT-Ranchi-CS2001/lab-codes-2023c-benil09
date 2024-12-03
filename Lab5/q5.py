"""
Enter the coordinates of two points on the cartesian plane (take user input
using comprehension). Find the equation of the straight line passing through
these points.

Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)

"""


x1, y1, x2, y2 = [float(coord) for coord in input("Enter the coordinates of two points (x1, y1, x2, y2) separated by spaces: ").split()]


if x1 == x2:
    equation = f"x = {x1:.2f}"
else:
    
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1  # y-intercept
    equation = f"y = {m:.2f}x + {c:.2f}" if c >= 0 else f"y = {m:.2f}x - {abs(c):.2f}"

# Print the equation of the line
print("The equation of the straight line is:", equation)

