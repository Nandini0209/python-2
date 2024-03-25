#Write a Python function to calculate the factorial of a number (a nonnegative integer).
def fact(x):
 fact=1    

 if x==1:
  return 1

 while x>1 :
   fact=fact*x
   x=x-1
 return fact


num=int(input("enter the number :"))
print("the factorial of the number is:",fact(num))        
