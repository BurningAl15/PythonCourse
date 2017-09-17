#Using variables
#greeting="Hello"
#greeting2=input("Write a greeting: ")
#print(greeting)
#print(greeting2)

#letters=input("Write a long word: ")
#maxVal=input("Enter a max value: ")

#print(maxVal)
#print(letters)
#Error
#print(letters[0:maxVal])
#letters3=letters.replace("a","e")
#letters2=letters.upper()
#print(letters3)
#[0:2] -> outputs a,b
#(a,b,c,d,e,f) ->common sorted array
#print(letters[0:2])
#[-2] -> outputs f
#(a,b,c,d,e,f)
#print(letters[-2])
#[-2] -> outputs f
#(a,b,c,d,e,f)
#print(letters[-2:])
#all letters since 1st (1,2,3,4,...)
#print(letters[1:])
#all letters until 3rd (0,1,2,3,...)
#print(letters[:3])

#if-elif-else statements
#index1=letters[0:12]
#index2=letters[0:5]

#if len(letters)<5:
#    print(index2)
#elif len(letters)>12:
#    print(index1)

#Using vectors
#x = [12,32,12,3,12,2,4,23,123,4,2,123,4,41,12,3,4,12,4,2334,2,312,23,4,12,2]

#Using functions
#print(sum(x))


#functions
#1
#def currency_converter(rate,euros):
#    dollars=rate*euros
#    return dollars

#val=currency_converter(1.42,5)
#print(val)

#2
#def minutesToHours(minutes):
#    hours=0
#    if(minutes/60>0):
#        times=minutes/60
#        hours+=1*int(times)
#        minutes-=60*int(times)
#    return hours,minutes

#def time(minutes,seconds):
#    hours=minutes/60 + seconds/3600
#    return int(hours)

#min=input("How much minutes: ")
#secs=input("How much secs: ")
#print(minutesToHours(int(min)))
#print(time(int(min),int(secs)))

#3
#def converting(celsius):
#    farenheit=celsius*9/5 + 32
#    return farenheit

#cel=input("Enter the number of celsius grades: ")
#print(converting(int(cel)))

#Exercises
#money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
#print(money["under_bed"][1])

#Problema UVA simple
a=input()

for x in range(int(a)):
    b=input()
    c=input()

if(b>c):
    print(">")
elif(b<c):
    print("<")
elif(b==c):
    print("=")
