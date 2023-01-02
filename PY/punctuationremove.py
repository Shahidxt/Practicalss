
puncuation = """!@#$%^&*()_+-=`~{[]}:;"'\|/?.,*"""
mystr = input("Input String : ")
no_pun = ''

for char in mystr:
    if not char in puncuation:
        no_pun+=char
        
        
print(no_pun)