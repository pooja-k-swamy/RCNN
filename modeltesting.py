from __future__ import print_function

import h5py
import PIL
from PIL import Image
import numpy as np

import pickle

import keras
from keras.datasets import cifar10
from keras.models import load_model
from keras.preprocessing import image 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

import PIL
from PIL import Image , ImageOps


nw = 25
nh = 25

model = load_model('keras_cifar10_trained_model3.h5')
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])


file = open("xtest.pkl", "rb")

x_data = []
imx = []

##img = Image.open('imgtt8301.jpg')
##img = np.array(img)
##img.resize(1,25,25,3)
###img1 = img1.append(img)
##x_data = img
##x_data = np.array(x_data)
##print (x_data.shape)

for i in range (0,6061):
    imx=pickle.load(file)

    oldSize = imx.size

    if (oldSize[0] > nw ) and (oldSize[1] > nh):
            img3 = imx.resize((nw,nh) , PIL.Image.LANCZOS)
            #imgname1 = "img.jpg"
            #img3.save(imgname1)

    else:

        #img3 = Image.open('original-image.png')
        deltaw=nw-oldSize[0]
        deltah=nh-oldSize[1]
        ltrb_border=(deltaw/2,deltah/2,deltaw-(deltaw/2),deltah-(deltah/2))
        img3 = ImageOps.expand(imx,border=ltrb_border,fill='black')
        #imgname1 = "img.jpg"
        #img_with_border.save(imgname1)
        
    #imx = Image.open("img.jpg")
    imx = np.array(img3)
    #imx = np.array(imx)
    ##img = Image.fromarray(imx, 'RGB')
    ##img.show() 
    #imx.resize(25,25,3)

    ##img = Image.fromarray(imx, 'RGB')
    ##img.show() 
    ##    print (x_train)
    x_data.append(imx)


file.close()




x_data = np.array(x_data)

x_data = x_data.astype('float32')
#x_test = x_test.astype('float32')
x_data /= 255
#x_test /= 255

pred = model.predict(x_data)

classes = model.predict_classes(x_data)

file = open("predict.pkl", "wb")
pickle.dump(classes,file)
file.close()


print("output:" , classes)

print(type(x_data))
print (pred)



