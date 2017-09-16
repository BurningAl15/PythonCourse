#Open the file in read mode
#print("-------------Using read-------------")
#f=open("sample3.txt","r")
#f.read()
#f.seek(0)
#print(f.read())
#f.close()

#print("\n")

#readlines is used for take strings and get them in lists
#print("-------------Using readlines-------------")
#f=open("sample3.txt","r")
#content=f.readlines()
#f.seek(0)
#print(content[1])
#print(content[0])
#rstrip is used to hide values you don't want to appear in your code when u r reading a file
#content=[i.rstrip("\n") for i in content]
#print(content)
#f.close()


#print("\n")
#g=open("Cover.png","r")
#print("Using write mode")
#g=open("writeSample.txt","w")
#g.write("Hi motherfucker")
#g.write("Hi motherfucker")
#h=["damn nigga", "i'm tired of fucking idiots like u"]
#g.write("\n")
#g.write(str(h))
#g.write("\n")
#g.write(h[0])
#g.write("\n")
#g.write(h[1])
#g.close()
#g=open("writeSample.txt","r")

#print(g.read())

#r opens a file for reading only. The file pointer is placed at the beginning of the file. this is the default mode
#r+ opens a file for both reading and writing. the file pointer placed at the beginning of the file
#w opens a file for writing only. overwrites the file if the file exists. if the file does not exist, creates a new file for writing.
#w+ opens a file for both writing and reading. overwrites the existing file if the file exists. if the file does not exist, creates a new file for reading and writing
#a opens a file for appending. the file pointer is at the end of the file if the file exists. that is, the file is the append mode. if the file does not exist, it creates a new file for writing
#a+ opens a file for both appending and reading. the file pointer is at the end of the file if the file exists. the file opens in the append mode. if the file does not exist, it creates a new file for reading and writing


#Exercise
temperatures=[10,-20,-289,100,12,4,23,5112,5,6,12,5,613,53]

def Converting(val):
    value=val*9/5 + 32
    if(value<-273.15):
        print("The value is not admited, is lower than absolute zero")
        value=0
    return value

g=open("Exercise.txt","w")

for i in temperatures:
    print(Converting(i))
    g.write(str(Converting(i))+ "\n")

g.close()
