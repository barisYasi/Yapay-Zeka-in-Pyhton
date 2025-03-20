import numpy as np

dizi = np.array([1,2,3,4,5]) #manuel olarak dizi oluşturmaya yarıyor
print(dizi)

# dizi = np.arange(0,11,1) #0,11 arasında 1 er ardışık ile yazdırıyor
# print(dizi)

# dizi = np.linspace(0,100,5) #istediğin sayı aralığını istediğin parçaya bölüyor
# print(dizi)

boyut = dizi.ndim
veri_turu = dizi.dtype
print(f"Dizinin boyutu : {boyut}")
print(f"Dizinin veri türü : {veri_turu}")

