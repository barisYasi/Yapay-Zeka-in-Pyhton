import numpy as np
dizi1 = np.array([1,2,3,4,5])
dizi2 = np.array([10,20,30,40,50])

toplam =np.add(dizi1,dizi2)
fark = np.subtract(dizi2,dizi1)
carpim = np.multiply(dizi1,dizi2)
bölüm = np.divide(dizi2,dizi1)

print(toplam)
print(fark)
print(carpim)
print(bölüm)

# Üst alma işlemi :
üst_al =np.power(dizi1,2)
print(üst_al)

#karekök alma :
karekok = np.sqrt(dizi2)
print(karekok)

# VARYANS: Değerin ortalamaya olan uzaklığına denir.
# Varyansı hesaplamak için var kısayolunu kullanırız numpyde :)

varyans = np.var(dizi2)
print(varyans)

# Standart sapma : Her ay satılan 10.000 çikolata sayısı 30.000 e çıktığı zaman standart sapması + yönde artmış denir
standart_sapma = np.std(dizi2)
print(standart_sapma)