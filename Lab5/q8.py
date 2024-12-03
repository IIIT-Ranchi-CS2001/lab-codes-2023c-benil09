"""
Sort the list of tuples constructed above with and without sorted function.
"""


customer_names = [f"Customer_{i}" for i in range(1, 6)]
customer_ids = [100 + i for i in range(5)]
shopping_points = [10 * i for i in range(5)]

customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

print("Original List of Tuples using zip():", customer_data_zip)
print("Original List of Tuples without using zip():", customer_data_manual)

sorted_with_sorted = sorted(customer_data_zip, key=lambda x: x[2])


customer_data_manual_sorted = customer_data_manual[:]
for i in range(len(customer_data_manual_sorted)):
    for j in range(len(customer_data_manual_sorted) - i - 1):
        if customer_data_manual_sorted[j][2] > customer_data_manual_sorted[j + 1][2]:
            customer_data_manual_sorted[j], customer_data_manual_sorted[j + 1] = (
                customer_data_manual_sorted[j + 1],
                customer_data_manual_sorted[j],
            )

# Print the sorted lists
print("Sorted List of Tuples using sorted():", sorted_with_sorted)
print("Sorted List of Tuples without using sorted():", customer_data_manual_sorted)