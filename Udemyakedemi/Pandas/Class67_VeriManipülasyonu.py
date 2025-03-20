import numpy as np
import pandas as pd

#Excel dosyasındaki verileri çekelim...
df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\TuncayErol_Pandas\Pandas\teknolojik_urunler1.xlsx')

#Bu dosyadaki eksik verileri alalım.
eksik_veriler = df.isnull()
#True döndürmesinin sebebi biz yukarıda soruyoruz eksik mi diye o da true yani evet eksik veya false hayır eksik değil diye cevap veriyor
print(eksik_veriler)

#Eksik verilerin olduğu satırları siliyoruz.
temiz_df = df.dropna()
print(temiz_df)

#Boş olan değerlere 0 atıyoruz.
#fillna() fonskiyonunda parantezin içerisine koyulan ne ise onu yazıyor oraya 
doldurulmus_df = df.fillna("Değer YOk")
print(doldurulmus_df)

df['Fiyat (TL)'] = df['Fiyat (TL)'].astype(float)
print(df.dtypes)

#Yeni sutün ekleme işlemi
df.insert(2,"Baris Yasin",range(1,21))
print(df)

#Excel dosyamıza yeni veri ekleyerek (sutün biçiminde) kaydetme işlemi
df.to_excel('ToExcel.xlsx',index=False)
print("DOsyanız kaydedildi ...")

df_düsük_deger = df.sort_values('Fiyat (TL)',ascending=False)
print(df_düsük_deger)

#Pandasta kullanılan 15 civarında popüler fonskiyonalr var bunlara hakim olup birkaç örnek ve doğru syntax kullanımı ile veri işleme konusunun büyük bir alanına hakim olabilirsin.