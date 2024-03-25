#Write a Python program to find the highest 3 values in a dictionary
d1={"a1":12,"a2":98,"a3":34,"a4":56,"a5":45}
d2 = dict(sorted(d1.items(), key=lambda x: x[1]))
print(list(d2))
print("*"*80)
print(d2(:-1)

