import numpy as np
import pandas as pd 

#Excel dosyasını oku
df = pd.read_excel(r'C:\Users\BarisYasin\Desktop\AKEDEMİK\Udemyakedemi\teknolojik_urunler_zamanli.xlsx')
# print(df)

#tarih sutününü datatime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# indeksleme (Çok Önemli !)                 
df.set_index('Tarih',inplace=True)
# print(df)

#Tarih sırasına göre verileri sıralayalım
df = df.sort_index()
# print(df)

#En yüksek satış yapılan ay ve o ayda satılan ürünler
aylık_satis = df.resample('ME')['Satış'].sum()
max_ay = aylık_satis.idxmax()
max_satis_ay = aylık_satis.max()
max_satis_ay_urunler = df[df.index.to_series().between(max_ay - pd.offsets.MonthBegin(1) , max_ay)]
# print(f"En yüksek satış yapılan ay : {max_ay} - Toplam satış : {max_satis_ay}")
# print("O ayda satılan ürünler : ")
# print(max_satis_ay_urunler [['Ürün Adı' , 'Satış']])

# print('-'*50)

#En düşük satış yapılan ay ve o ayda satılan ürünler
min_ay = aylık_satis.idxmin()
min_satis_ay = aylık_satis.min()
min_satis_ay_urunler = df[df.index.to_series().between(min_ay - pd.offsets.MonthBegin(1) , min_ay)]
# print(f"En düşük satış yapılan ay : {min_ay}")
# print("O ayda satılan ürünler : ")
# print(min_satis_ay_urunler [['Ürün Adı' , 'Satış']])

#En çok satış yapılan gün ve o günde satılan ürünleri bulmaya çalışacağız...
daily_salary = df.resample('D')['Satış'].sum()
max_gün = daily_salary.idxmax()
max_salary_daily = daily_salary.max()
max_salary_daily_product = df.loc[max_gün]
print(f"En yüksek satış yapılan gün : {max_gün} - Toplam Satış : {max_salary_daily}")
print("O günde satılan ürünler : ")
print(max_salary_daily_product [['Ürün Adı','Satış']])


