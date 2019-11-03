
myList = ["Adana", "Ankara", "İstanbul"]

print("*"*30)

for item in myList:
    print(item)

print("*"*30)

myList.append("Mardin")
for item in myList:
    print(item)

print("*"*30)

print(len(myList))

print("*"*30)

myList.remove("Adana")
print(myList)