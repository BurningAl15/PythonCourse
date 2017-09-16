#Lists
#listA=[12,"hello","Nigger"]
#print(listA)
#listA.append("Damn")
#print(listA)
#listA.remove(12)
#print(listA)

#varName.count(#ofOcurrences)
#print(listA.count(12))
#print(len(listA))
#listA=[123,23,4,2,1,4,412,3,4]
#print("Not sorted: ", listA)
#listA.sort()
#print("Sorted: ", listA)
#Tuples
#tuplA=(12,"hello","Nigger")

#print(len(tuplA))

#Diccionaries
#d={"Name":("John","Aldhair"),"Surname":"Smith"}
#l=[2,3,4]
#print(d)
#print(d["Name"])
#print(d["Surname"])

#
#abc=[["Aldhair Vera Camacho"],["Nancy Angela Rojas Salvatierra"]]
#a=abc[0]
#b=abc[1]
#c=["Aldhair Vera Camacho"]
#print(len(abc[0][0]))
#print(abc[0:2])
#print(len(a[0]))
#print(len(b[0]))
#val=0
#for i in abc:
#    for j in i:
#        print(abc[val][0])
#        val+=1

#for i in abc:
#    print(a[0])

#List of strings
#spam=["cat","dog","moose"]
#print(len(spam[0]))
#print(len(spam[1]))
#print(len(spam[2]))
#print(len(spam[0])+len(spam[1])+len(spam[2]))

#print("Tocando el primer elemento del arreglo: " + spam[0])
#print("Tocando el primer y el segundo elemento del arreglo: " + str(spam[0:2]))

#print("\n")
#for i in spam:
#    print(i)

#Working in Lists
#catNames=[]#Se crea una lista vacia
#while True:#Bucle infinito
    #Imprime: Enter the name of the cat (tamaño del arreglo + 1)
#    print("Enter the name of the cat " + str(len(catNames) + 1) + ' (Or enter nothing to stop): ')
    #Ingresa el nombre
#    name=input()
    #Si no se presiona nada, se rompe el bucle
#    if(name==""):
#        break
    #Se ingresa el nombre al arreglo.
#    catNames=catNames+[name]
#Los nombres de los gatos son:
#print("The cat names are: ")
#llama a todos los nombres de los gatos
#for name in catNames:
#    print(" " + name)

#Same but using method append()
#catNames=[]
#while True:
#    print("Enter the name of the cat "+ str(len(catNames)+1)+" (or enter nothing to stop): ")
#    name=input()
#    if(name==""):
#        break
#    catNames.append(name)

#print("The cat names are: ")
#for name in catNames:
#    print(" "+ name)

###############################################
#Using for loops in lists
#supplies=["engine","wheels","lights"]
#for i in range(len(supplies)):
#    print("Index" + str(i) + " in supplies is: " + supplies[i])

#Methods
#spam=["hello","hi","howdy","heyas"]
#a=spam.index("hello")
#b=spam.index("heyas")

#print(spam[a]+ " - "+ str(a) +"\n" +spam[b] + " - " + str(b))
#spam.append("Twoody")

#for i in range(len(spam)):
#    print(spam[i] + " - " + str(i))


#spam=["a"]
#spam.insert(1,"b")
#for i in range(len(spam)):
#    print(spam[i])

#stuff={"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}

def Display(inventory):
    print("Inventary")
    itemTotal=0
    for k,v in inventory.items():
        print(k,v)
        itemTotal+=v

    print("Total number of items: " + str(itemTotal))

#Display(stuff)

dragonLoot=["gold coin","dagger","gold coin","gold coin","ruby"]


def addToInventary(inventory,itemAdded):
    val=0
    for i in range(len(itemAdded)):


    for k,v in inventory.items():
        if(itemAdded[val]==k):
            v+=1
            print("Pase por aqui 1")
        elif(itemAdded[val]!=k):
            #inventory.items()
            print("Pase por aqui 2")
        val+=1

inv={"gold coin":42,"rope":1}
#Display(inv)
addToInventary(inv,dragonLoot)
Display(inv)

#picnicItems={"apples":5,"cups":2}
#print(str(picnicItems.get("cups",0)))
