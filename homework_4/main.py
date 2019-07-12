"""
Homework Assignment #4: Lists

"""

#unique list of elements
myUniqueList = []

#elements that didnt get added to list
myLeftovers = []

#add elements to an array
def addToUniqueList(el):
    added_flag = False
    if el not in myUniqueList:
        myUniqueList.append(el)
        added_flag = True
    return added_flag

def addLeftOvers(el):
    myLeftovers.append(el)


def addElements(el):
    if(addToUniqueList(el)):
        print(el, " added to unique list")
    else:
        addLeftOvers(el)
        print(el, " added to leftovers")


addElements(1)
addElements(2)
addElements(1)
addElements(1.1)
addElements("hello")
addElements("hello")

print('Unique element list: ',myUniqueList)
print('Leftovers list: ',myLeftovers)