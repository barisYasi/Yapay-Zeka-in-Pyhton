import numpy as np

#Satılacak kitapların fiyatları
kitap_fiyatları = np.array([25,30,50,40,15,80,100])

#Satılan kitapların adeti
satis_adetleri = np.array([100,150,170,135,140,200,380])

#Kitap Kategorileri
kategoriler = np.array(["Roman","Şiir","Çocuk","Tarih","Bilim","Akedemik","Şiir"])

toplam_gelir = kitap_fiyatları * satis_adetleri
print("Toplam kitap satışlarından elde edilen gelir : ",kategoriler,'\n',toplam_gelir)

#En pahalı kitap fiyatını yazalım
en_pahalı_kitap = np.max(kitap_fiyatları)
print("En pahalı kitap fiyatı : ",en_pahalı_kitap,"TL")

#Kitap fiyatlarının ortalamsını yazalım
ortalam_fiyat = np.median(kitap_fiyatları)
print("Ortalama bir adet kitap fiyatı : ",ortalam_fiyat,"TL")

#En ucuz kitap fiyatını yazalım.
en_ucuz_kitap = np.min(kitap_fiyatları)
print("En uygun kitap fiyatı : ",en_ucuz_kitap,"TL")

roman_fiyatları = kitap_fiyatları[kategoriler == "Roman"]
roman_satis_adedi = satis_adetleri[kategoriler == "Roman"]
roman_kazancı = roman_fiyatları * roman_satis_adedi 
print("Roman fiyatları : ",roman_fiyatları,"TL","\n","Roman satış adedi : ",roman_satis_adedi,"\n","Romandan kazanılan ücret : ",roman_kazancı)


veri = np.array([satis_adetleri,kitap_fiyatları])
veri_reshaped = np.reshape(veri,(2,7))
print(veri_reshaped)