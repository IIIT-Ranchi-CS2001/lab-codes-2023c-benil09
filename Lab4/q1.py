"""
Find the number of palindrome words in the given sentence without defining
any new function (feel free to use python’s in-built functions).

"""


sentence = input("Enter a sentence: ")
palindrome_count = 0
words = sentence.split()
for word in words:
    if word == word[::-1]:
        palindrome_count += 1

print(f"The number of palindrome words is: {palindrome_count}")