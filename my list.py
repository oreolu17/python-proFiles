# List Assignment
myUniqueList = []
myUniqueList.append(60)
myUniqueList.append(70)
myUniqueList.append(80)
myUniqueList.append(90)
myUniqueList.append(100)
print(myUniqueList)

def AddToList(item):
    flag = False
    for i in myUniqueList:
        if i == item:
            flag = True#Item already exists
    if(flag == False):
        myUniqueList.append(item)

AddToList(70)
AddToList(40)
AddToList(30)

print(myUniqueList)