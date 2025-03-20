import numpy as np

dizi1 = np.array([1,2,3,4,5,4])
dizi2 = np.array([5,6,7,8,9,10])

# toplam = dizi1 + dizi2
# cikarma = dizi1 - dizi2
# çarpma = dizi1 * dizi2
# bölme = dizi1 / dizi2

# print(toplam)
# print(cikarma)
# print(çarpma)
# print(bölme)

toplam = np.sum(dizi1+dizi2)
print(toplam)

carpim = np.prod(dizi1)
print(carpim)

karekok = np.sqrt(dizi1)
print(karekok)

aritmatik_ortalama = np.mean(dizi1)
print(aritmatik_ortalama)

medyan_al = np.median(dizi1)
print(medyan_al)

standartsapma = np.std(dizi1)
print(standartsapma)