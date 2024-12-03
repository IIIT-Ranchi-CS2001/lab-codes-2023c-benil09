"""
Define a function my_zip() that can form a list of tuples by iterating the
following customer details:-
‘customer Name, customer ID , shopping points’
and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done
only if all lists are of equal length. If strct = False, zipping can be done by taking
the minimum length of the iterable.
"""


def my_zip(*iterables, strct=False):
   
    if strct:
        lengths = [len(it) for it in iterables]
        if len(set(lengths)) != 1:
            raise ValueError("All lists must have the same length for strict zipping.")
    min_length = min(len(it) for it in iterables)
    return [tuple(it[i] for it in iterables) for i in range(min_length)]


customer_name = ["Alice", "Bob", "Charlie"]
customer_id = [101, 102, 103]
shopping_points = [150, 200, 250]


print(my_zip(customer_name, customer_id, shopping_points, strct=True))


customer_name = ["Alice", "Bob", "Charlie"]
customer_id = [101, 102]
shopping_points = [150, 200, 250]

print(my_zip(customer_name, customer_id, shopping_points, strct=False))