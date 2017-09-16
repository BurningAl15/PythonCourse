import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb=cv2.imread("img.jpg")
img_rgb=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2RGB)
R=img_rgb;

#Mostrando canales
#Canal Rojo
def Rojo(R):
    R[:,:,1:3]=0

#Verde
V=img_rgb
def Verde(V):
    V[:,:,0]=0
    V[:,:,2]=0

#Verde(R)

#Azul
A=img_rgb
def Azul(A):
    A[:,:,0:2]=0

#Gris
#def Gris(R):
img_gris=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
img_gris=cv2.cvtColor(img_gris,cv2.COLOR_GRAY2BGR)

#Gris2
"""R=R[:,:,0].astype('int')
G=V[:,:,1].astype('int')
B=A[:,:,2].astype('int')
img_gris2=(R+G+B)/3
img_gris2=img_gris2.astype('uint8')
img_gris2=cv2.cvtColor(img_gris2,cv2.COLOR_GRAY2BGR)"""


#Iluminacion
"""img_hsv=cv2.cvtColor(img_rgb,cv2.COLOR_RGB2HSV)
img_intensidad=np.zeros(img_hsv.shape)
img_intensidad[:,:,0]=256-img_hsv[:,:,2]
img_intensidad[:,:,1]=256-img_hsv[:,:,2]
img_intensidad[:,:,2]=256-img_hsv[:,:,2]"""

#Histograma
hist=np.zeros(256)
#gris=img_gris[:,:,0]
#rojo=img_rgb[:,:,0]
#verde=img_rgb[:,:,1]
#azul=img_rgb[:,:,2]
#########
#y,x=gris.shape
#y,x=verde.shape
#y,x=azul.shape
"""for i in range(0,x):
    for j in range(0,y):
        #hist[gris[j,i]] +=1
        #hist[rojo[j,i]]+=1
        #hist[verde[j,i]]+=1
        hist[azul[j,i]]+=1
plt.plot(range(256),hist,color='r')"""

#valores unicos
#unique,counts=np.unique(gris,return_counts=True)
#unique,counts=np.unique(rojo,return_counts=True)
#plt.plot(unique,counts)



#Imprimir
#plt.imshow(img_intensidad)
#plt.axis('off')
plt.show()
