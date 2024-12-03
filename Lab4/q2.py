"""
Create a list of int using list comprehension [multiple input from keyboard].
Find the mean, median, and mode of the given list ( usage of specific modules
such as statistics is strictly prohibited.)
"""

numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
n = len(numbers)
numbers.sort()
mean = sum(numbers) / n
median = numbers[n // 2] if n % 2 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2
mode = max(set(numbers), key = numbers.count)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")  
