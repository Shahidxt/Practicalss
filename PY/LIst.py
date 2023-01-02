#Python List Operations

#Creating List with Mix data type
AList = [1,2,3,"four",5,6,"seven",8,9,"ten",11,2,666,887,46,8,1,6,True]

#Printing Whole List
# print(AList)


#           Access item using item
item = AList[1]
item2= AList[9]

#accessing last item in list
item3 = AList[-1]

#accessing second last item in list
item4 = AList[-2]

#accessing third last item in list
item4 = AList[-3]


#                List Slicing
#Slicing from index 4 to end including index 4
Slice = AList[1:]

#Slicing from Strting Index to 4 not including index 4
Slice2 = AList[:4]

#Slicing from Strting Index 5 to 12 not including index 12
Slice3 = AList[5:12]


#       Adding to Item to list

#Adding item in the last
AList.append("added")
AList.append(416551)

#Adding using Index
AList.insert(0,"modify")
AList.insert(5,"modify 5")

#extending to another List
Secondlist=["SecondlistItem1","SList2",False,"Sheab"]
AList.extend(Secondlist)
AList.extend(["aaad","fffasf",654,False])


#Changing Values using index
AList[0]= "AlistMOdifiedusingIndex"
AList[-1] = "LAstModi"

#Deleting first 2 item using index
del AList[:1]

#deleting last item using index
del AList[-1]

#deleting using value
AList.remove(1)
AList.remove("SecondlistItem1")
AList.remove("added")

#removing last item using pop and return value
remove1= AList.pop()
remove2= AList.pop()

#removes all item from list
# AList.clear()

#return the index of first match value
matchIndex = AList.index(True)
matchInde2 = AList.index("SList2")

#returns count of specific items in list
count = AList.count(True)
count2 = AList.count("seven")

#sort the list condition: List should one datatype example int or string...
# AList.sort()

#reverses the the list item.
AList.reverse()


#Returns the copy of list.
Copy_list = AList.copy()


#Iterating through list
for item in AList:
    #dosomething with each item in list.
    pass
    
    
#check if item in list
result = "four" in AList
result2 = 141 in AList


#List Comprehension 
NewComp = [str(value) + "_Added" for value in AList] 
NewComp2 = [str(value) + " X" for value in AList]

print(AList)

