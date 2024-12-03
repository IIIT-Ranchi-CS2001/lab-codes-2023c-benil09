"""

Define a function my_sort() to sort the list of tuples created using my_zip
function in the last question. The function must have two types of arguments- the
list that carry the data, the key that determines the argument of sorting:
[Usage of built-in function sorted() is a punishable offense]

Key = 0: sorting based on customer name in ascending order

Key = 1: sorting based on Customer ID

Key = 2: sorting based on shopping points

"""
from q1 import my_zip 

def my_sort(data, key=0):
   
    # Perform bubble sort on the data
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                # Swap tuples if they are out of order
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# Example usage
customer_name = ["Alice", "Bob", "Charlie"]
customer_id = [104, 103, 102]
shopping_points = [250, 200, 210]

# Generate the list of tuples using my_zip
data =my_zip(customer_name, customer_id, shopping_points, strct=True)

print("\nOriginal Data:",data)


# Sort by customer name
print("\nSorted by Customer Name:",my_sort(data, key=0))


# Sort by Customer ID
print("\nSorted by Customer ID:",my_sort(data, key=1))


# Sort by Shopping Points
print("\nSorted by Shopping Points:",my_sort(data, key=2))
