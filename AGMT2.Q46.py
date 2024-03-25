'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':  
300}, o {'item': 'item1', 'amount': 750}]  
Expected Output: 
Counter ({'item1': 1150, 'item2': 300})'''

def combine_values(list_of_dicts):
    result = {}
    for d in list_of_dicts:
        item = d['item']
        amount = d['amount']
        result[item] = result.get(item, 0) + amount
    return result


data = [{'item': 'item1', 'amount': 400},
               {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}]


combined_values = combine_values(data)


print("Expected Output:")
print(combined_values)
