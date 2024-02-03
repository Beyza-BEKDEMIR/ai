import matplotlib.pyplot as plt                   #tepe tırmanma(hill climbing) algoritması 
import numpy as np
import random

def fonk(x):
    return np.cos(8*x-0.3)-x**2+0.2*x    # iki yıldız üs alma

alt_sinir=-3
ust_sinir=3

x=np.linspace(alt_sinir, ust_sinir,100) 
         
y=fonk(x)     
plt.plot(x,y)

baslangic_x=random.uniform(-3,3)        #hill climbing için önce bir başlangıç noktası seçmek gerekiyor.
baslangic_y=fonk(baslangic_x)

plt.scatter(baslangic_x,baslangic_y, color='red')

gorus_mesafesi=0.2  
kabul_edilen = 0

for adim in range(1000):   
    hareket=random.choice([-gorus_mesafesi, gorus_mesafesi]) #-1 ile 1 arasında rastgele değer üretir. ama tam sayıya yuvarlar

    sonraki_x=baslangic_x + hareket
    sonraki_y=fonk(sonraki_x)

    if(sonraki_y> baslangic_y):
        kabul_edilen +=1
        baslangic_x=sonraki_x
        baslangic_y=sonraki_y

        plt.scatter(baslangic_x, baslangic_y, color="green")

plt.title(f'{kabul_edilen} adımda x:{baslangic_x} y:{baslangic_y}')
plt.show()

