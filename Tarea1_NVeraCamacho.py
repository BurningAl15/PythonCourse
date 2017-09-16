import cv2
import numpy as np
def cargar(link): #Load picture
    img = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
import matplotlib.pyplot as plt
def show(temp):
    plt.imshow(temp)
    plt.show()
    return
img=cargar('face.png')
#show(img)

yiq=[[0.299,0.587,0.114],[0.596,-0.275,-0.321],[0.212,-0.523,0.311]]
rgb=[[1,0.956,0.621],[1,-0.272,-0.647],[1,-1.107,1.704]]


for i in range(0,np.size(img,0)):
    for j in range(0,np.size(img,1)):
        #img[i][j]=np.dot(img[i][j],yiq)
        #img[i][j]=np.dot(img[i][j],rgb)
        img[i][j]=np.dot(yiq,img[i][j])
        img[i][j]=np.dot(rgb,img[i][j])

show(img)
