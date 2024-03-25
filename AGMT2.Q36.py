# How Do You Check The Presence Of A Key In A Dictionary?

d1={1:"nan",2:"div",3:"sak",4:"mih",5:"vip"}
print(d1)
key=int(input("enter the key you want to check:"))
if key in d1.keys():
    print("key is present is the dictionary!!!")
else:
    print("key is  not present is the dictionary!!!")
