import pandas as pd

df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\TuncayErol_Pandas\Pandas\teknolojik_urunler.xlsx')
print(df.head())

# #Fiyatlar kategorisinden fiyatı 5000'tlden yüksek olanları alalım
# df_fiyat_ust = df[df['Fiyat (TL)'] > 5000]
# print(df_fiyat_ust)

# #Fiyatı 500 tlnin üstünde olan ve satışları da 6 dan fazla olan ürünleri yazdıralım.
# df_filtrele = df[(df['Fiyat (TL)'] > 5000) & (df['Satış'] > 6 ) ]
# print(df_filtrele)

# #Fiyatı 500 TLden yüksek olan ve kategoriside bilgisiyarlar olan dataları yazdır
# df_filtre2 = df[(df['Fiyat (TL)'] > 5000) & (df['Kategori'] == 'Bilgisayarlar')]
# print(df_filtre2)

# #.loc fonskiyonu şu anlama geliyor yani locala gidiyoruz ve devamında : var o da öncekilerin veya sonralarının bir önemi yok benim isteddiklerimi ver diyor.Onu da yazdık zaten
# df_secili = df.loc[ : , ['Ürün Adı','Fiyat (TL)']]
# print(df_secili)

# #.iloc fonskiyonu ile sıra istediğimiz ilk sıraları alıyoruz.Burada 5 dedik onun için 5 e kadar olanları aldık gibi...
# df_ilk = df.iloc[: 5 , :]
# print(df_ilk)

# #DataFrame üzerinden sorgu yapıyoruz.. Sadece sorgu işlemleri ama ...
# df_sorgu = df.query('Satış>10')
# print(df_sorgu)          

#Belirli bir kategoride veri arama işlemi yapan fonskiyona .isin() fonskiyonu denir.Fakat sayısal değerlerin üzerinde bu fonksiyonu kullanmayız aramayı daha çok string söze değerlerde kullanırız
df_kategori = df[df['Kategori'].isin(['Bilgisayalar','Mobil Cihazlar'])]
print(df_kategori)


