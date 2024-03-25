#Write a Python program to returns sum of all divisors of a number
l=[]
sum=0
num=int(input("enter the number:"))

for i in range (1,num//2+1):
   if num%i==0:
    l.append(i)  

print("list is:",l)

for i in l:
    sum+=i
    
print(sum)




