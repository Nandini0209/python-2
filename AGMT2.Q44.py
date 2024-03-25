'''Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.  
Sample data: {'1': ['a','b'], '2': ['c','d']} '''
from itertools import product

def display_combinations(data):
    keys = data.keys()
    value_lists = [data[key] for key in keys]
    combinations = product(*value_lists)
    
    for combination in combinations:
        print(''.join(combination))

data = {'1': ['a', 'b'], '2': ['c', 'd']}

display_combinations(data)
