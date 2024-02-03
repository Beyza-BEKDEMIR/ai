import matplotlib.pyplot as plt                   #tepe tırmanma(hill climbing) algoritması
import numpy as np
import random

def fonk(x):
    return (x**2)+4*x    # iki yıldız üs alma

alt_sinir=-10
ust_sinir=10

x=np.linspace(alt_sinir, ust_sinir,100) #iki sınır arasında 100 tane değer oluşturacak
#x=np.array([2,3,5,7])           # sayısal değerlerde numpy kullanılır. dizilerde vb.
y=fonk(x)     

plt.plot(x,y)
#plt.plot.scatter(x,y) #renklerini değiştiriyor

baslangic_x=random.uniform(-10,10)        #hill climbing için önce bir başlangıç noktası seçmek gerekiyor.
baslangic_y=fonk(baslangic_x)

plt.scatter(baslangic_x,baslangic_y, color='red')

gorus_mesafesi=1  #görülebilen mesafe 1 m dir. 1 m aşağı veya yukarı gidilebilir.
kabul_edilen = 0

for adim in range(100):   #bu işlem 100 kere gerçekleşecek yani 100 hareket olacak.
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
