#Write a Python program to print all unique values in a dictionary.

d1={1:"nan",2:"mih",3:"nan",4:"sak",5:"vip"}
unique=[]
l=d1.values()
#print(l)
print(d1,)

print("*"*80)

for i in l:
    if i not in unique:
     unique.append(i)
    else:
         pass
print(unique)        
         
