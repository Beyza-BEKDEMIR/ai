import numpy as np

x1=np.array[1,1,2,3,4,5]
x2=np.array[1,1,2,3,4,5]
y=np.array[1,1,2,3,4,5]
Mu=0.2

print(x1)
print(x2)
print(y)

def sigmoid(deger):
    return 1/(1+np.exp(-deger)) 

np.random.seed(100) #her random değer ürettiğinde hep o random değeri kullanır her seferinde değer değişmez.
w1=np.random.random()
w2=np.random.random()
wb=np.random.random()

print(w1)
print(w2)
print(wb)

net=x1[0]*w1+x2[0]*w2+wb
print(net)

yhat=sigmoid(net)
print(yhat)

hata=y[0]-yhat
print(hata)

w1=w1+Mu*hata*x1[0]
w2=w2+Mu*hata*x2[0]
wb=wb+Mu*hata*1

print(w1)
print(w2)
print(wb)

"""
for epoch in range(10):
    print(f'Epoch: {epoch} ------------')
    for i in range(6):
        net=x1[0]*w1+x2[0]*w2+wb
        yhat=sigmoid(net)
        hata=y[0]-yhat
        w1=w1+Mu*hata*x1[0]
        w2=w2+Mu*hata*x2[0]
        wb=wb+Mu*hata*1
        print(f'{i}. iter -> hata:{hata}')  """    