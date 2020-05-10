import pickle
from time import sleep

file = open("ytest.pkl", "rb")

imx=pickle.load(file)

file.close()


file = open("predict.pkl", "rb")

pre=pickle.load(file)

file.close()

j = 0.0

for i in range (0,6061):
    print imx[i],pre[i]
    print i 
    if imx[i] == pre[i]:
        j = j + 1


print (j/6061)
    
