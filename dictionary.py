# 29. Write a Python program to merge two dictionaries into one.


dict1 = {'a': 3, 'b': 2}  # First dictionary
dict2 = {'c': 4, 'd': 5}  # Second dictionary

dict1.update(dict2) # updated the data to dict2... in order to merge


# The merged dictionary will be printed
print("Merged Dictionary:", dict1)