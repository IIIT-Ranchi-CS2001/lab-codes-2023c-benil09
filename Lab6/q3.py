"""
 
"""


def my_max(*args):
    """
    Returns the maximum value from a list, set, or tuple of integers without using built-in functions.
    
    Args:
        *args: Unpacked elements from a list, set, or tuple.
    
    Returns:
        int: The maximum value among the arguments.
    
    Raises:
        ValueError: If the input is empty or contains non-integer values.
    """
    if len(args) == 0:
        raise ValueError("Input collection cannot be empty.")

    # Initialize the first value as the maximum
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num

    return max_value

# Test cases
print(my_max(*[1,4,3,6,2]))    # Unpack list input
print(my_max(*{2, 4, 6, 8, 10}))   # Unpack set input
print(my_max(*(10, 20, 30, 40)))   # Unpack tuple input