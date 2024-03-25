#Write a Python script to check if a given key already exists in a dictionary.

d1={1: 'nan', 2: 'div', 3: 'har', 4: 'sak', 5: 'mih'}
print(d1)
key=int(input("enter the key that you want to check:"))

if key in d1:
    print("the key exists in the dictionary")
else:
    print("the key does not exists in the dictionary")
