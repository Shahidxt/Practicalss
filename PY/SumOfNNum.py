

#Q1
def SquareSum(num):
    """
    Returns the sums of first n numbers.
    
    """
    
    sum=0
    for i in range(1,num+1):
        sum+=i*i
    return sum

# print(SquareSum(4))


#Q2


import os 
def MergeFile():
    path =os.getcwd()
    d1=d2= ""
    with open(f'f.txt',"r") as d:
        d1= d.read()
        
    with open("2.txt",'r') as f:
        d2=f.read()
        
    file = d1+ "\n"+d2
    with open("3rd.txt","w") as ee:
        ee.write(file)
    return True
