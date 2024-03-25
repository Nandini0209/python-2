 #Write a Python function to check whether a number is perfect or not.
'''A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
For example, 6 is a perfect number because the sum of its proper divisors (1, 2, 3) equals 6.'''



def function(x):
 result=[]
 s=0     
 for i in range(1,x//2+1):
    if x%i==0:
     result.append(i)
 print(result)
   
 for i in result:
    s += i
 
 if x>=1 and s==x:
  print("number",num," is a perfect number",)
 else:
    print("number",num,"not perfect number")

num=int(input("enter the number:"))
function(num)     
    
    
   
