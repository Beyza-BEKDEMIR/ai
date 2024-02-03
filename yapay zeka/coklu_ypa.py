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

def sigmoid(deger):
    return 1/(1+np.exp(-deger))

netA=x1[0]*w1A+x2[0]*w2A+wA
fA=sigmoid(netA)
netB=x1[0]*w1B+x2[0]*w2B+wB
fB=sigmoid(netB)
netC=fA*wAC+fB*fB+wC
yhat=sigmoid(netC)
print(yhat)

hata=y[0]-yhat
deltaC= hata*yhat*(1-yhat)
deltaA=deltaC*wAC
deltaB= deltaC*wBC
dwAC=Mu*deltaC*fA
wAC=wAC-dwAC
dwBC=Mu*deltaC*fB
wBC=wBC-dwBC
dwC=Mu*deltaC*(1)
wC= wC-dwC

dw1A=Mu*deltaA*x1[0]
w1A =w1A - dw1A
dw2A= Mu * deltaA * x2[0]
w2A = w2A - dw2A
dwA = Mu * deltaA*(1)
wA = wA - dwA

dw1B=Mu*deltaB*x1[0]
w1B =w1A - dw1B
dw2B= Mu * deltaB * x2[0]
w2B = w2B - dw2B
dwB = Mu * deltaB*(1)
wB = wB - dwB



