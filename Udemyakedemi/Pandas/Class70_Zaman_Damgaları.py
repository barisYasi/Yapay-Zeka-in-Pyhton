import numpy as np
import pandas as pd

df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\TuncayErol_Pandas\Pandas\teknolojik_urunler.xlsx')

# print(df)

#Şimdi eşittirin sol kısmında Tarih diye yeni bir başlık ekledik.
#to_datetime fonskiyonu ile pandastan zamanları çekebilmek için bir kütüphanye bağlandık
#np.random.choice ile numpy kütüphanesinden random olarak seçim yaoptık.
#np.data_range ile hangi zaman dilimleri aralığında olduğunu işaretledik
#Size = len(df) diyerekte uzunluğunun dataframe ile aynı uzunlukta olması gerektiiğini yazdık

df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('01.01.2025','31.12.2025'), size = len(df)))
print(df)

df.to_excel('teknolojik_urunler_zamanli.xlsx',index = False)
print("Veriler dosyaya aktarıldı...")
