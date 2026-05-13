dict={}
for i in range(6):
    x=int(input("Enter a Marks: "))
    dict.update({i:x})
print("Subject=",i+1,dict)


dict2={}
x=int(input("Enter Physics Marks: "))
dict2.update({"Physics" : x})

x=int(input("Enter chemistry Marks: "))
dict2.update({"chemistry" : x})

x=int(input("Enter Biology Marks: "))
dict2.update({"Biology" : x})

x=int(input("Enter SST Marks: "))
dict2.update({"SST" : x})

x=int(input("Enter English Marks: "))
dict2.update({"English" : x})
print(dict2)