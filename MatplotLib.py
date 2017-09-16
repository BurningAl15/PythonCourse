year=[1,2,4,4,5,5,6,1,23,5,1,2,456,3,12]
pop=[31,4,12,54,1,24,5,23,5,1,5,63,6,23,63]
# Print the last item from year and pop
#year.sort()
#pop.sort()
#print(year[-1])
#print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import math
v=[]
v2=[]

for i in range(2000,3000,4):
    v.append(math.sqrt(i))
    v2.append(i*i*3)

#plt.hist(pop,bins=3)
#plt.clf()
#plt.hist(pop,bins=9)

#Dibujar una grafica usando lineas
#plt.plot(v,v2)
#plt.clf()
#Dibuja una grafica de dispersion
#plt.scatter(v,v2)
#plt.clf()
plt.title("Graphic")
plt.ylabel("Year")
plt.xlabel("Population")

plt.yticks([0,2,4,6,8,10])
plt.xticks([0,0.5])
plt.hist(v2,bins=15)
# Scatter plot
#plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Additional customizations
#plt.text(1550, 71, 'India')
#plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)



# Display the plot with plt.show()
plt.show()



#Indice
#clear plot
#plt.clf()
#Dibuja (plot-una linea) y (scatter-una grafica por dispersion)
#Dibujar una grafica usando lineas
#plt.plot(v,v2)
#Dibuja una grafica de dispersion
#plt.scatter(v,v2)
#Sirve para poner el titulo a la grafica
#plt.title("Graphic")
#Sirve para poner nombres a los parametros que se miden en la grafica (x e y)
#plt.ylabel("Year")
#plt.xlabel("Population")

#Setea numeros en la escala
#plt.yticks([0,2,4,6,8,10])
#plt.xticks([0,0.5])

#Hace que las escalas de la grafica esten en base logaritmica
#plt.xscale("log")
#plt.yscale("log")
# Display the plot with plt.show()
#plt.show()
