#Write a Python script to concatenate following dictionaries to create a new one.
d1={1:"nan",2:"div",3:"har"}
d2={4:"sak",5:"mih"}
print(d1)
print(d2)
d3=d1|d2 #union operator
d1.update(d2)#update function
print(d1)
print(d3)
