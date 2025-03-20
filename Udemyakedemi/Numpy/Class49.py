class okul:
    def __init__(self):
        self.şube=input("Lütfen şubeyi giriniz : ")
        self.öğretmen=input("Lütfen öğretmeni giriniz : ")
        self.kıdem=input("Lütfen kıdemi giriniz :")
        self.bölüm=input("Lütfen bölümü giriniz : ")
        self.mevcut=int(input("Lütfen mevcutu giriniz : "))
        self.maaş=int(input("Lütfen maaşı giriniz : "))

    def bilgileri_göster(self):
        print("-" * 45)
       
        print("ŞUBE : {}\nÖĞRETMEN : {}\nBÖLÜM : {}\nMEVCUT : {}\nMAAŞ : {}\nKIDEM : {}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut,self.maaş,self.kıdem))
        print("-"*45)

    def branş_değiş(self):
        print("**ESKİ BRANŞ** {}",format(self.bölüm))
        yeni_branş=input("Lütfen yeni branşı giriniz :")
        self.bölüm = yeni_branş
        print("** YENİ BRANŞ **  {}".format(self.bölüm))
    
    def maaş_göster(self):
        print(f"{self.öğretmen}'isimli öğretmenin maaşı : {self.maaş} TL")

class müdür(okul):
    def __init__(self):
        super().__init__()
    
    def bilgileri_göster(self):
        return super().bilgileri_göster()
    
    def kıdem_değiş(self):
        print("**ESKİ MEVKİ** {}",format(self.kıdem))
        yeni_kıdem=input("Lütfen yeni kıdemi giriniz :")
        self.kıdem = yeni_kıdem
        print("** YENİ BRANŞ **  {}".format(self.kıdem))
    
    def zam_yap(self):
        print(f"Zam yapma ekranına hoşgeldiniz Sayın : {self.öğretmen}")
        zam_miktarı = int(input("Lütfen zam yapmak istediğiniz miktarı giriniz :"))
        self.maaş += zam_miktarı
        print(f"{self.öğretmen} isimli öğretmenin yeni maaş miktarı :{self.maaş} TL' dir.")

while True:
        seçim_yap = input("1-Öğretmen Girişi :\n2-Yönetici Girişi:")
        
        if seçim_yap == "1":
            ''''
            şube=input("Lütfen şubeyi giriniz : ")
            öğretmen=input("Lütfen öğretmeni giriniz : ")
            kıdem=input("Lütfen kıdemi giriniz :")
            bölüm=input("Lütfen bölümü giriniz : ")
            mevcut=int(input("Lütfen mevcutu giriniz : "))
            maaş=int(input("Lütfen maaşı giriniz : "))
            '''
            print("LÜtfen yapmak istediğiniz tercihi giriniz :")
            tercih_yap=input("1-Bilgileri Göster : \n2-Kıdem Değiş : \n3-Zam Yap : \n4-Branş Değiştir : \n5-Maaş Göster : \n")

            if tercih_yap == "1":
                öğretmen = müdür()
                öğretmen.bilgileri_göster()
            elif tercih_yap == "2":
                öğretmen = müdür()
                öğretmen.kıdem_değiş()
            elif tercih_yap == "3":
                öğretmen = müdür()
                öğretmen.zam_yap()
            elif tercih_yap == "4":
                öğretmen = okul()
                öğretmen.branş_değiş()
            elif tercih_yap == "5":
                öğretmen=okul()
                öğretmen.maaş_göster()
            else:
                print("Yanlış giriş yaptınız ... ")
            

        elif seçim_yap == "2":
            print("LÜtfen yapmak istediğiniz tercihi giriniz :")
            tercih_yap=input("1-Bilgileri Göster : \n2-Kıdem Değiş : \n3-Zam Yap : \n")
            if tercih_yap == "1":
                yönetici = müdür()
                yönetici.bilgileri_göster()
            elif tercih_yap == "2":
                yönetici = müdür()
                yönetici.kıdem_değiş()
            elif tercih_yap == "3":
                yönetici = müdür()
                yönetici.zam_yap()
            else:
                print("Yanlış giriş yaptınız ... ")
                
        else:
            print("Hatalı giriş yaptınız ...")

        son_karar = input("İşleme devam etmek istiyor musunuz ? (E\H)").lower()
        if son_karar == "e":
            continue
        elif son_karar =="h":
            print("Allaha Emanet olun :")
            break