#Write a Python program to find the repeated items of a tuple.

T=(1,2,1,4,5,2,6,8,7,8,9)
print(T) 
for i in T:
    if T.count(i) > 1:
        print("REPEATED items ",i," is:",T.count(i))
          
        
    
