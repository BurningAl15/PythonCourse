#Lambda
#a=lambda x:x**2
#print(a(2))

#print("First form")
#eats=["japFood","thaiFood","chinesseFood"]
#print("----------")
#for ate in eats:
#        if 'japFood' in ate:
#           print(ate)
#print("\n")
#print("Second form")
#print("----------")
#for x in range(0,3):
#       print("something")

#print("\n")
#print("Using while")

#var=int(input("Ingrese la cantidad maxima de iteraciones: "))
#while(var>0):
#    print(var)
#    var-=1

#1
#def name(a):
#    sum=0
#    for x in range(0,a):
#        sum += x
#    print(sum)

#a=int(input())
#name(a)

#2
#def name(a):
#    sum=0
#    for x in a:
#        sum += x
#    print(sum)
#    print(max(a))
#    print(min(a))

#a=[18,19,2,1]
#name(a)

#while
#password=''
#while password != 'python123':
#    password=input("Enter password: ")
#    if(password == 'python123'):
#        print("You are logged in")
#    else:
#        print("Sorry, try again")

#for
#names=['james','john','jack']
#email_domains=['gmail','hotmail','yahoo']

#for i,j,z,w in zip(names,email_domains,reversed(names),reversed(email_domains)):
#    print(i,j)

#print("\n")
#for z,w in zip(reversed(names),reversed(email_domains)):
#    print(z,w)

#Exercise
#function
#def converting(celsius):
#    if(celsius < -273.15):
#        print("That temperature does not make sense")
#    else:
#        farenheit=celsius*9/5 + 32
#        return farenheit
#List of values
#temperatures=[10,-20,-289,100]

#Iterations
#for i in temperatures:
#    print(converting(i))

#Conditionals
#spam=0

#b=[9,7,8,2,4,2,3,5]
#a=7
#c=int(input("Ingrese la cantidad de iteraciones: "))
#while(c <= 7):
#    print("# de iteracion: ", c)
#    c+=1
#    print(b[a])
#    a-=1

#name=''
#a=0
#name=input()
#while a <= len(name)-1:
#    print(name[a])
#    a+=1

#Usando package random
#import random

#def getAnswer(answerNumber):
#    if(answerNumber==1):
#        return "It is certain"
#    elif(answerNumber==2):
#        return "It is decidely so"
#    elif(answerNumber==3):
#        return "Yes"
#    elif(answerNumber==4):
#        return "Reply hazy try again"
#    elif(answerNumber==5):
#        return "Ask again later"
#    elif(answerNumber==6):
#        return "Concentrate and ask again"
#    elif(answerNumber==7):
#        return "My reply is no"
#    elif(answerNumber==8):
#        return "Outlook not so good"
#    elif(answerNumber==9):
#        return "Very doubtful"

#r=random.randint(1,9)
#fortune=getAnswer(r)
#print(fortune)

#Adivina el numero
#import random
#secretNumber=random.randint(1,20)
#print("Estoy pensando en un numero entre 1 y 20")

#for guessesTaken in range(1,7):
#    print("Toma una pista")
#    guess=int(input())

#    if(guess > secretNumber):
#        print("Tu numero es muy alto")
#    elif(guess<secretNumber):
#        print("Tu numero es muy bajo")
#    else:
#        break

#if(guess==secretNumber):
#    print("Buen trabajo! Adivinaste mi numero en  " + str(guessesTaken) + " intentos")
#else:
#    print("No, el numero que pense era: " + str(secretNumber))

#La secuencia Collatz
#def collatz(number):
#    value=0
#    if(number%2==0):
#        value=number//2

#    elif(number%2==1):
#        value=number*3+1
#    return value

#val=int(input())
#while(val!=1):
#    print(collatz(val))
#    val=collatz(val)
