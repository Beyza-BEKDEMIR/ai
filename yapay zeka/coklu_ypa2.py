import numpy as np

x1=np.array([1,1,2,4,4,3,5,5,6,7])
x2=np.array([1,3,2,1,3,5,2,3,4,1])
y=np.array([0,0,1,1,1,0,1,1,0,0])

np.random.seed(50)
w1A=np.random.random()
w1B=np.random.random()
wA=np.random.random()
w2A=np.random.random()
w2B=np.random.random()
wB=np.random.random()
wAC=np.random.random()
wBC=np.random.random()
wC=np.random.random()

Mu=0.2
alfa=0.3
dw1A=0
dw2A=0
dwA=0
dw1B=0
dw2B=0
dwB=0
dwAC=0
dwBC=0
dwC=0

def sigmoid(deger):
    return 1/(1+np.exp(-deger))

for epoch in range(100):
    for i in range(10):
        netA=x1[i]*w1A+x2[i]*w2A+wA
        fA=sigmoid(netA)
        netB=x1[i]*w1B+x2[i]*w2B+wB
        fB=sigmoid(netB)
        netC=fA*wAC+fB*wBC+wC
        yhat=sigmoid(netC)
        
        hata=y[i]-yhat
        print(f'      {i}. iter----> hata:{hata}')
        deltaC= hata*yhat*(1-yhat)
        deltaA=deltaC*wAC
        deltaB= deltaC*wBC
        dwAC=Mu*deltaC*fA+alfa+dwAC
        wAC=wAC-dwAC
        dwBC=Mu*deltaC*fB+alfa+dwBC
        wBC=wBC-dwBC
        dwC=Mu*deltaC*(1)
        wC= wC-dwC+alfa*dwC

        dw1A=Mu*deltaA*x1[i]+alfa*dw1A
        w1A =w1A - dw1A
        dw2A= Mu * deltaA * x2[i]+alfa*dw2A
        w2A = w2A - dw2A
        dwA = Mu * deltaA*(1)+alfa*dwA
        wA = wA - dwA

        dw1B=Mu*deltaB*x1[i]+alfa*dw1B
        w1B =w1A - dw1B
        dw2B= Mu * deltaB * x2[i]+alfa*dw2B
        w2B = w2B - dw2B
        dwB = Mu * deltaB*(1)+alfa*dwB
        wB = wB - dwB



