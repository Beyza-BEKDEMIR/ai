import numpy as np

x1=np.array([1,1,2,3,4,5])
x2=np.array([3,4,5,1,1.5,3])
y=np.array([1,1,1,0,0,0])
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

for epoch in range(10):
    print(f'Epoch: {epoch} ------------')
    toplamHata=0
    for i in range(6):
        net=x1[i]*w1+x2[i]*w2+wb
        yhat=sigmoid(net)
        hata=y[i]-yhat
        w1=w1+Mu*hata*x1[i]
        w2=w2+Mu*hata*x2[i]
        wb=wb+Mu*hata*1
        print(f'{i}. iter -> hata:{hata}') 
        toplamHata=toplamHata+np.abs(hata) #hataların mutlak değerini aldık çünkü + lar ile - ler bibirini götürüyor. 
        
    if toplamHata<(0.05):
        break   

def test(x1,x2):
    net=x1*w1+x2*w2+wb
    yhat=sigmoid(net) 
    return yhat  
        
print(test(3,8))
print(test(3,3.5))
print(test(4,100))
print(test(100,4))

