#zuky = 2
#print(zuky)
#print(float(zuky))

#gato=input()
#print(gato)
"""
if(float(gato)%2 == 0):
    print("es par")
elif(int(gato)%2==1):
    print("es impar")
else:
    print("no es par")
gato1=int(gato)


while(gato1 != 10):
    print(gato1)
    gato1+=1

alpha=[1,123,4,1,4,213,41,5,12,5,12,45,12,5,12,45]
beta="saoindoiahndoihasoidaiodsoiasdhasiod"
theta=["ajf","ajf","ajf","ajf"]

d="jsjid"
e="asohdio"

f=d+" "+e

gamma=open("sample.txt","r")

gamma.seek(0)

print("* * * ")
print("* * ")
print("* ")"""
#print('''Hi, my name is Barry Allen and I'm the fastest man Alive

#The flash''')

#spam='damn'
#spam2=spam.upper()
#print(spam2)
#print(spam2.lower())
#spam3=124

#print(spam.isalpha())
#print(str(spam3).isdecimal())

#Exercise
"""while True:
    print("Enter your age: ")
    age=input()
    if age.isdecimal():
        break
    print("Please enter a number for your age. ")

while True:
    print("Select a new password (letters and numbers only):")
    password=input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")"""

#startswith() and endwith() methods
print("Hello world!".startswith("Hello"))
print("Hello world!".endswith("world!"))

#join and split
abc=["cats","rats","bats"]
b="alhds,askkasd,kasooasd"
print(", ".join(abc))
print(b.split(","))

#
import pyperclip
pyperclip.copy(b)
print(pyperclip.paste())
