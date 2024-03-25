#Write a Python function to get the largest number, smallest num and sum of all from a list.

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
l.sort()
print("changed list:",l)
print("the smallest number in the list is:",l[0])
print("the largest number in the list is:",l[-1])
sum=l[0]+l[1]+l[2]+l[3]+l[4]+l[5]
print("the sum is:",sum)

