''' Write a Python program to create a dictionary from a string.  
Note: Track the count of the letters from the string.  
Sample string: 'w3resource'  
Expected output:  
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

def create_letter_count_dict(input_string):
    letter_count = {}
    for char in input_string:
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

sample_string = 'w3resource'


result_dict = create_letter_count_dict(sample_string)

print("Expected output:")
print(result_dict)
