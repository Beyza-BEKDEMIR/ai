import matplotlib.pyplot as plt                   #benzetimli tavlama algoritması 
import numpy as np
import random

def fonk(x):
    return np.cos(8*x-0.3)-x**2+0.2*x    # iki yıldız üs alma

alt_sinir=-3
ust_sinir=3

x=np.linspace(alt_sinir, ust_sinir,100) 
         
y=fonk(x)     
plt.plot(x,y)

baslangic_x=random.uniform(-3,3)        
baslangic_y=fonk(baslangic_x)

plt.scatter(baslangic_x,baslangic_y, color='red')
T=10
gorus_mesafesi=0.2 
kabul_edilen = 0 

eniyi_x=baslangic_x     #En iyi pozisyonu başlangıç pozisyonu olarak belirliyoruz.
eniyi_y= baslangic_y
while T>0.01:    #tavlama benzetimli algoritması
    
    for adim in range(100):  
        hareket=random.uniform(-gorus_mesafesi, gorus_mesafesi) 

        sonraki_x=baslangic_x + hareket                        #daha iyi sonuç için
        if (sonraki_x>ust_sinir):                              #adım sayısını arttırma
            sonraki_x=ust_sinir                                #görüş mesafesini genişletme
        if (sonraki_x<alt_sinir):
            sonraki_x=alt_sinir
        sonraki_y=fonk(sonraki_x)

        if(sonraki_y> baslangic_y):
            kabul_edilen +=1
            baslangic_x=sonraki_x
            baslangic_y=sonraki_y
            plt.scatter(baslangic_x, baslangic_y, color="green")

            if sonraki_y>eniyi_y:
                eniyi_x=sonraki_x
                eniyi_y =sonraki_y

        else:         # metropolis algoritması
            w=(np.exp(-(sonraki_y- baslangic_y)/T)-1)*10
            r=random.random()  # 0 ile 1 arasında değer üretiyor.
        
            if w>r:
                kabul_edilen +=1
                baslangic_x=sonraki_x
                baslangic_y=sonraki_y
                plt.scatter(baslangic_x, baslangic_y, color="yellow") #sarı olanlar kötü hareketler
                if sonraki_y > eniyi_y:
                    eniyi_x=sonraki_x
                    eniyi_y=sonraki_y


T=T*0.1
plt.title(f'{kabul_edilen} adımda x:{baslangic_x} y:{baslangic_y}')
plt.scatter(baslangic_x,baslangic_y, color="brown")
plt.show()
