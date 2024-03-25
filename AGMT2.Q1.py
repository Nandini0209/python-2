#What is List? How will you reverse a list? 

'''list is basically a group of different type of data .It is mutable data type where we can change or replace the data from the given data.
It is generally present in the sqaure bracket and the indexing always starts with zero.'''

l=[]
l2=[]
l1=input("enter the data:")
l.append(l1)
l1=input("enter the data:")
l.append(l1)
l1=input("enter the data:")
l.append(l1)
l1=input("enter the data:")
l.append(l1)
l1=input("enter the data:")
l.append(l1)
l1=input("enter the data:")
l.append(l1)
print("original list:",l)
l2=l[::-1]
print("the reversed list:",l2)


