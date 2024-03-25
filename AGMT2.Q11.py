#Write a Python function that takes a list and returns a new list with unique elements of the first list
U=[]
def function(x):
   for i in l:
       if i not in U:
          U.append(i)
   return U
l=[1,2,3,4,3,2,6,7,77,8]
print("the original list is:",l)
print("the new list is",function(U))
