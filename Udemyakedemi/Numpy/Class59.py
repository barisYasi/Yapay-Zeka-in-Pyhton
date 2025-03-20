import numpy as np
dizi = np.array([10,20,30,40,50,60,70,80,90,100])

# boolen_mask = dizi >= 50
# print(boolen_mask)

#Boolen maskı kullanarak dizideki elemanları seçme...
# secilmis = dizi[boolen_mask]
# print("50' DEN BÜYÜK OLAN ELEMANLAR : " , secilmis)

#Çoklu eleme işlemi :
boolen_mask2 = (dizi>=30 ) & (dizi<=100)

print("20 İLE 110 ARASINDAKİ SAYILAR : ",dizi[boolen_mask2])