#Write a Python program to check multiple keys exists in a dictionary
d={1:"nandini",2:"sakshi",3:"divya",4:"sahil",5:"mihir",6:"falgun"}
k=["1","2","3","4"]
for k in d:
 if k in d:
 print("keys are present in the dictionary")
 else:
 print("keys are not present in the dictionary")
