#Write a Python program to remove duplicates from a list.

l=['2','3','2','4','5','10']
unqlist=[]
for i in l:
     if i not in unqlist:
        unqlist.append(i)
        
print("the origianl list is:",l)
print("the unique list is:",unqlist)


    
