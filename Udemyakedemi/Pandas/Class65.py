import numpy as np
import pandas as pd

#seri oluşturalım
s = pd.Series([10,20,30,40], index=['a',"b","c","d"])
print(s)

data = {
    'Fiyat' : [10,80,30,40],
    'Satış Adedi' : [18,1500,39,97],
    'Kategori': ["Roman","Şiir","Çocuk","Akedemik"]
}
df = pd.DataFrame(data)
# # print(df)

# #Dataframe hakkında bilgi veriyor
# print(df.info())

# #Dataframein başındaki ilk elemanları yazdırıyor 
# print(df.head())

# #Datafreamin detaylı bilgilerini veriyor standart sapma max min değer vs. vs.
# print(df.describe())

# #sadece o seçtiklerimi yazdır veya görselleştir anlamına geliyor.
# print(df[['Fiyat','Kategori']])

# #Datafreame içinde fiyatı 50'den yüksek olan verileri göster
# filtre = df[ df ['Fiyat'] > 50 ]
# print(filtre)


# #Toplam Fiyat diye bir sutün ekleyerek onu da tabloya yazdırıyoruz
# df['Toplam Fiyat'] = df['Fiyat'] * df['Satış Adedi']
# print(df)

# #Drop komutu o dataframeden bir sutün silmek için kullanıyor.Axis = 1 diye kullanmamızın sebebi ise 1 sutün sil manasında
# df = df.drop('Kategori',axis=1)
# print(df)

df['Toplam Satış'] = df['Satış Adedi'] * df['Fiyat']
print(df)

df = df.drop('Kategori',axis=1)
print(df)

df['Kategori'] = ["Roman","Şiir","Çocuk","Akedemik"]
print(df)
