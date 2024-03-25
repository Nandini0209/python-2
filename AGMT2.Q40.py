#Write a Python program to map two lists into a dictionary
l1=[1,2,3,4,5]
l2=["nan","sak","mih","har","piy"]
print(l1)
print(l2)
print("********************************************************")
A=dict(map(lambda x: (x[0], x[1]), zip(l1, l2)))
print(A)
