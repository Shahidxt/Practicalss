#Tuple operations

#empty tuple 
ATuple = ()

#tuple with value,
# a tuple value cannot be modify
ATuple=(1,2,3,5,6,"hello","shahid","last")

#above code and below is same affected, 
# parentheses is optional.
ATuple=(1,2,3,5,6,"hello","shahid","last")

#Accessing tuple value using index
item = ATuple[1]
item2 = ATuple[-1]
item3 = ATuple[4]

#Slicing as same as list
ST= ATuple[:4]
ST2 = ATuple[3:]
ST3 =ATuple[2:5]

#Count
count = ATuple.count("shahid")
count2 = ATuple.count("last")

#Iterating through Tuple
for item in ATuple:
    #dosomething wait every item in list
    pass


#check wheather item existed in tuple
found = 'shahid' in ATuple
found2 = "scdc" in ATuple

#iterating thorugh tuple is fast as compare to list
#tuples data cant to modified or changed 

