import numpy as np
import pandas as pd

#Excel dosyasını oku
df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\TuncayErol_Pandas\Pandas\teknolojik_urunler.xlsx')
print(df)

#Analiz işlemleri yaparken gruplandırmayı daha çok kullanırız çünkü veriyi belli parçalara ayırmak o veriyi işleme ve inceleme konusunda daha yararlı bir işlem olur

gruplar = df.groupby('Kategori')

#Kategori kısmından satışların toplamını bana göster
toplam_satış = df.groupby('Kategori')['Satış'].sum()
print(toplam_satış)

#Kategori sutünündan bana fiyatların toplamını göster
toplam_satış_fiyat = df.groupby('Kategori')['Fiyat (TL)'].sum()
print(toplam_satış_fiyat)

#Kategori sutünundan bana satışların ortalmaasını göster
ortalama_satis_fiyat = df.groupby('Kategori')['Fiyat (TL)'].mean()
print(ortalama_satis_fiyat)

#Kategori bölümünden satışın toplamını fiyatın da ortalmaasını aldık.
#.agg fonskiyonu ile birden fazle işlemi tek bir fonksiyon ile tamamladık
#.agg fonksiyonundan sonra {} ile sözlük oluşturduk.
toplama_ve_ortalama = df.groupby('Kategori').agg({
    'Satış' : 'sum',
    'Fiyat (TL)' : 'mean'
})
print(toplama_ve_ortalama)

#.loc fonskiyonu neye göre seçim yapacağımızı belirliyor şimdi burada diyoruz ki biz 'Kategori' ismine göre seçim yapacağız 
#.ixmax ile de en pahalı ürünü seçiyoruz
en_pahali_urun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
print(en_pahali_urun)

#Toplam satışı 50 den büyük olan kategorileri yazırmak istiyorum diyorum.
#filter ve lambda ifadeleri ile bir for döngüsü oluşturduk orada
hype_sell = df.groupby('Kategori').filter(lambda x:x['Satış'].sum() > 50)
#Print kısmına çift kareli parantez açarak spesifik olarak yazdırmak istediğimiz sutünları,grupları yazdırıyoruz
print(hype_sell[['Kategori','Ürün Adı','Satış']])

