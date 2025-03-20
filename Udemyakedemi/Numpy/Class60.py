import numpy as np

dizi1 = np.array([1,2,3])
dizi2 = np.array([4,5,6])

#concatenate fonskiyonu tek boyutlu fonskiyonları birleştiriyor.

birlesik_dizi = np.concatenate((dizi1,dizi2))
print("Diziler birleştirildi :",birlesik_dizi)

#2 boyutlu dizileri birleştirme
#hstack isimli fonskiyon ise 2 boyutlu dizilerin birleştirilme işlemini sağlıyor.
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])

#hstack fonskiyonu yatay olarak birleştiriyor.
birlestirilmis_dizi = np.hstack((array1,array2))
print(birlestirilmis_dizi)

print("-"*50)

#vstack fonskiyonu dikey olarak birleştiriyor.
birlestirilmis_dizi2 = np.vstack((array1,array2))
print(birlestirilmis_dizi2)

# tek boyutlu dizilerde diziyi eşit parçaya bölme işlemi "split" fonsiyonu ile oluyor.
dizi = np.array([1,2,3,4,5,6])
bölünmüs_dizi = np.split(dizi,3)
print(bölünmüs_dizi)

#İki boyutlu dizilerde eşit parçaya yatay bölme işlemi "hsplit"fonskiyonu ile oluyor.
dizi = np.array([[1,2,3,4],[5,6,7,8]])
ikibytlu_split_dizi = np.hsplit(dizi,2)
print(ikibytlu_split_dizi)


#İki boyutlu dizilerde eşit parçaya dikey bölme işlemi "vsplit"fonskiyonu ile oluyor.
dizi = np.array([[1,2,3,4],[5,6,7,8]])
ikibytlu_split_dizi = np.vsplit(dizi,2)
print(ikibytlu_split_dizi)