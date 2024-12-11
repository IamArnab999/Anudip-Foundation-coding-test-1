# 29. Write a Python program to merge two dictionaries into one.


# Function
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Created a copy of dict1
    merged_dict.update(dict2) # updated the data to dict2... in order to merge
    
    return merged_dict  # It will return the merged dictionary

dict1 = {'a': 3, 'b': 2}  # First dictionary
dict2 = {'c': 4, 'd': 5}  # Second dictionary

# Stored the merged dictionary in a variable by calling the function
result = merge_dicts(dict1, dict2)

# The merged dictionary will be printed
print("Merged Dictionary:", result)