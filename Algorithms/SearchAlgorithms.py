#Binary search

#x=input()
l=[1,2,4,23,3,4,1,5,2,5,1,5,16,1,23,5,2,5,120]
mid=0

def validating(l):
    if(len(l)%2==0):
        mid=round(len(l)/2)
    elif(len(l)%2==1):
        mid=round((len(l)-1)/2)
    return mid

m=validating(l)


"""
a=0
for i in l:
    a+=1
    if(int(x)>m):
        if(int(x) == i):
            print(a)
            print(l[a])
    elif(int(x)<m):
        if(int(x) == i):
            print(a)
            print(l[a])
"""
print(m)

#print(m)
#print(l[m])
