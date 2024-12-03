"""
Enter three lists using list comprehension: Customer name, Customer ID,
and shopping points. Construct a list of tuples with and without using
built-in function zip().
"""


customer_names = [f"Customer_{i}" for i in range(1, 6)]
customer_ids = [100 + i for i in range(5)]
shopping_points = [10 * i for i in range(5)]

customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

print("List of Tuples using zip():", customer_data_zip)
print("List of Tuples without using zip():", customer_data_manual)