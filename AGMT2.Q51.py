#Write a Python function that checks whether a passed string is palindrome or not .

def pallindrome(x):

 s2=s1[::-1]
 if s1==s2:
   print("passed string is a pallindrome")
 else:
     print("passed string is not a pallindrome")


s1=input("enter a string:")
pallindrome(s1)
 
   
