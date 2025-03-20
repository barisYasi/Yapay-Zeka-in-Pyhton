import numpy as np
# dizi = np.array([1,2,3,4,5,6])

# #reshape fonskiyonu ile dizimizi istediğimiz boyutta şekillendirebiliyoruz.
# yeni_dizi = dizi.reshape((3,2))
# print(yeni_dizi)

# dizi = np.array([[1,2],[3,4],[5,6]])

# tek_boyut = dizi.reshape((-1))
# print(tek_boyut)

#reshape (3,-1) dediğimiz zaman 3 satır yap sütun sayısını ise sen hangisi doğru ise ayarla ve uygula demek istiyorum
dizi1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yeni_dizi1 = dizi1.reshape((3,-1))
print(yeni_dizi1)
