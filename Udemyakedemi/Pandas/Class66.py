import numpy as np
import pandas as pd

#excel dosyasını oku

df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\TuncayErol_Pandas\Pandas\teknolojik_urunler.xlsx')

#ilk birkaç satırı oku
print(df.head())

#Ortalama fiyatı hesaplayalım...
ortalama_fiyat = df['Fiyat (TL)'].mean()
print(f'Ortalama fiyat : {ortalama_fiyat} TL')

#Her grubun satışını yazdıralım
grup_bazli_satis = df.groupby('Kategori')['Satış'].sum()
print(grup_bazli_satis)

#En çok gelir sağlayan ürünü bulma ...
max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
print(max_gelir)

#Fiyatı 4000TL'den yukarı olan ürünleri almak istersek ne yapmalıyız ?
yüksek_fiyat = df[df['Fiyat (TL)'] >= 4000]
print(yüksek_fiyat)

#İstediğim kategoriyi aşağıdaki to.excel komutu ile yeni bir excel dosyası olarak oluşturup kaydettim klasörümde...
yüksek_fiyat.to_excel('Fiyatı_4000^den_yükseler_olanlar.xlsx',index = False)

#Tablodaki bir sutünü yazdıralım
ürün_adi = df['Ürün Adı']
print(ürün_adi)

#Kategorisine göre fiyatını yazdıralım
kategori_fiyatı = df.groupby('Kategori')['Fiyat (TL)'].apply(list).reset_index()
print(kategori_fiyatı)
