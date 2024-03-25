#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

L=[]
for i in range(1,31):
    num=i*i
    L.append(num)
print([L[0],L[-6:]])
