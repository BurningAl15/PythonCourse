r"""
Learning bout datetime and file using
"""
import datetime

"""

now=datetime.datetime.now()
v2=datetime.datetime(2017,5,14,11,19,39,583348)
v1=datetime.datetime.isoformat(now)
vdiff=now-v2
vX=now.strftime("%B %Y %d")
filename="abc.txt"
vsum=datetime.timedelta(days=1)
def create_file():
    #This function creates an empty file
    with open(vX+".txt","w") as file:
        file.write("")#Writing empty string

create_file()

print(now.strftime("%Y-%m-%d-%H-%M-%S-%f"))
print(now.strftime("%D"))
print(now.strftime("%B %Y %d"))
print(v1)
print(v2)
print(vdiff)
"""
"""
import time
lst=[]

for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

for i in lst:
    print(i)
"""

#Exercise

now=datetime.datetime.now()
v=now.strftime("%Y-%m-%d-%H-%M-%S-%f")

a=open("file1.txt","r")
b=open("file2.txt","r")
c=open("file3.txt","r")
alpha=a.read()+" "+b.read()+" "+c.read()

def create_file():
    with open(v+".txt","w") as file:
        file.write(alpha)#Writing empty string

create_file()
