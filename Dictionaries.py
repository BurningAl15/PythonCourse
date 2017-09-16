#Dictionaries
#myCat={"size":"fat","color":"gray","disposition":"loud"}
#like in a list, you can call a value using the key into the []
#print(myCat["size"])

#myCat={12345:"Luggage Combination",42:"The answer"}
#print(myCat[12345])

#Dictionaries vs lists
#Order is important
#spam=["cats","dogs","moose"]
#bacon=["dogs","moose","cats"]
#print(spam==bacon)

#Order in items is not important
#eggs={42:"The answer",12345:"Luggage Combination"}
#ham={12345:"Luggage Combination",42:"The answer"}
#print(eggs==ham)

#EXM
#birthdays={"Alice":"Apr 1","Bob":"Dec 12","Carol":"Mar 4"}

#while(True):
#    print("Enter a name: (blank to quit)")
#    name=input()
#    if(name==""):
#        break
#    if(name in birthdays):
#        print(birthdays[name] + " is the birthday of "+name)
#    else:
#        print("I do not have birthday information for " + name)
#        print("What is their birthday?")
#        bday=input()
#        birthdays[name]=bday
#        print("Birthday database updated.")


#using get() method
#spam={"name":"Zophie","Age":42}
#print(spam.get("name"))

###  EXM  ###
#usando pprint
#import pprint as pnt
#message=["Whatever","Whatever","Whatever"]
#dragonLoot=["golden coin","golden coin","simple knife","golden coin", "wand"]
#count={}
#for character in dragonLoot:
#    count.setdefault(character,0)
#    count[character]=count[character]+1

#print(count)
#Usando pprint
#pnt.pprint(count)

#Tic Tac Toe
#TheBoard={'Top-L':" ","Top-M":" ","Top-R":" ",
#          "Mid-L":" ","Mid-M":" ","Mid-R":" ",
#          "Low-L":" ","Low-M":" ","Low-R":" "}

#TheBoard={'1':" ","2":" ","3":" ",
#          "4":" ","5":" ","6":" ",
#          "7":" ","8":" ","9":" "}

#def printBoard(board):
#    print(board["1"] + " | " + board["2"] + " | " + board["3"])
#    print("--+---+--")
#    print(board["4"] + " | " + board["5"] + " | " + board["6"])
#    print("--+---+--")
#    print(board["7"] + " | " + board["8"] + " | " + board["9"])

#turn="X"
#for i in range(9):
#    printBoard(TheBoard)
#    print("Turn for " + turn + ". Move on which space?")
#    move=input()
#    TheBoard[move]=turn
#    if(turn=="X"):
#        turn = "O"
#    else:
#        turn = "X"
#printBoard(TheBoard)

#Nested dictionaries and lists
#allGuests={"Alice":{"apples":5,"pretzels":12},
#           "Bob":{"ham sandwiches":3,"apples":2},
#           "Carol":{"cups":3,"apple pies":1}}

#def totalBrought(guests,item):
#    numBrought=0
#    for k,v in guests.items():
#        numBrought=numBrought + v.get(item,0)
#    return numBrought

#print("Number of things being brought: ")
#print(" - Apples                " + str(totalBrought(allGuests,"apples")))
#print(" - Pretzels              " + str(totalBrought(allGuests,"pretzels")))
#print(" - Ham sandwiches        " + str(totalBrought(allGuests,"ham sandwiches")))
#print(" - Cups                  " + str(totalBrought(allGuests,"cups")))
#print(" - Apple pies            " + str(totalBrought(allGuests,"apple pies")))
#for i in allGuests.values():
#    for j in i.keys():
#        print(j+ "  " + str(totalBrought(allGuests,j ) ) )

#dragonLoot
dragonLoot=["gold coin","dagger","gold coin", "ruby"]
inventory={"gold coin":42,"rope":1,"dagger":2}
def DisplayInventory(inventory):
    print("Inventory: ")
    item_total=0
    for k,v in inventory.items():
        print(str(v) + " - " + k)
        item_total+=v
    print("Total number of items: " + str(item_total))
#DisplayInventory(inventory)

def SumValues(dict,value):
    sumatory=0
    sumatory+=dict.get(value,0)
    return sumatory

def addToInventory(inventory, addedItems):
    addedItems.sort()
    count={}
    Ninventory={}
    val=0
    #Pasar los valores de la lista a un diccionario
    for i in addedItems:
        count.setdefault(i,0)
        count[i]+=1
    #Revisar si los valores del diccionario inventory son diferentes de los de count
    #estos se agregan a Ninventory y visceversam y si son iguales, se hace una suma de valores
    for k,v in inventory.items():
        for k1,v1 in count.items():
            #if(k != k1):
            Ninventory.setdefault(k1,v1)   
            if(k == k1):
                val=SumValues(inventory,k) + SumValues(count,k1)
                Ninventory.setdefault(k,val)
            Ninventory.setdefault(k,v)
    #print(Ninventory)
    #if(inventory.get("gold coin",0) and count.get("gold coin",0)):
        #val=SumValues(inventory,"gold coin") + SumValues(count,"gold coin")
    #print(inventory)
    #inventory["gold coin"]=val
    #print(inventory)
    return Ninventory


inv=addToInventory(inventory,dragonLoot)
DisplayInventory(inv)
