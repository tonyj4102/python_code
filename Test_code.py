x=6
y=5
j =x*y
notCleaned=[]
l=0

tile=[]
for a in range(x):
    for b in range(y):
        tile[l] = (x,y)
        print tile
        l=l+1
print tile
    
for i in range(j):
    notCleaned= notCleaned +[i]
    
print notCleaned

pos =35
cleaned=[]

if pos in notCleaned:

    for k in notCleaned:
        if pos ==k:
            cleaned =cleaned+[k]
            del notCleaned[k]
        
            print notCleaned
            print cleaned
            




