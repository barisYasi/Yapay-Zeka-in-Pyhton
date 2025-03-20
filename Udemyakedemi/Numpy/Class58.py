# KÜMÜLATİF : Bir önceki veriler ile en sonki veriyi toplayarak son bir sonuç elde eden tabire denir.

import numpy as np
dizi = np.array([1,2,3,4,5,1000])

maks = np.max(dizi)
print("Dizi üzerindeki en yüksek değere sahip veri : ",maks)
min = np.min(dizi)
print("-"*50)
print("Dizi üzerindeki düşük değere sahip veri : ",min)

#dizideki elemanları toplar.
toplam = np.sum(dizi)

#Dizideki elemanları her bir basamakta kümülatif olarak toplarzaryo...
kume_toplam = np.cumsum(dizi)
print(kume_toplam)
