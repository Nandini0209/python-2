#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

l=['nandini','ananya','sakshi','1221','mihir','alia']
count=0
for i in l:
    if len(i)>=2 and i[0]==i[-1]:
        count=count+1
    
print(l)   
print("the number of string is:",count)   


