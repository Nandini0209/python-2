#Write a Python function that takes two lists and returns true if they have at least one common member.

def function(L1,L2):
 result=False    
 for x in L1:
    for y in L2:
       if x==y:
        result=True   
        return result
L1=[1,2,3,4,5,6,7]
L2=[1,55,66,3,2,67]
print("the list having member is",function(L1,L2))    
