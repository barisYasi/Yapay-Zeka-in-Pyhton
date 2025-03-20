class okul:
    def __init__(self,şube,öğretmen,bölüm,mevcut):
        self.şube=şube
        self.öğretmen=öğretmen
        self.bölüm=bölüm
        self.mevcut=mevcut

    def bilgileri_göster(self):
        print("-"*45)
        print("SINIF BİLGİLERİ : ")
        print("ŞUBE : {}\nÖĞRETMEN : {}\nBÖLÜM : {}\nMEVCUT : {}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("-"*45)
    
    def branş_değiş(self):
        yeni_branş=input("Lütfen yeni branşınızı giriniz : ")
        print("***ESKİ BRANŞ***",self.bölüm)
        self.bölüm=yeni_branş
        print("-"*45)
        print("SINIF BİLGİLERİ : ")
        print("ŞUBE : {}\nÖĞRETMEN : {}\nBÖLÜM : {}\nMEVCUT : {}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("-"*45)


while True:
    sınıf_oluştur = input("Lütfen bir sınıf oluşturarak isim veriniz :")
    sınıf_şube = input("Lütfen sınfın şubesini giriniz :")
    öğretmen_isim = input("Lütfen öğretmenin ismini giriniz :")
    sınıf_bölümü = input("Lütfen sınıfın bölümünü seçiniz :")
    sınıf_mevcut = int(input("Lütfen sınıfın mevcudunu giriniz :"))

    sınıf_oluştur=okul(sınıf_şube,öğretmen_isim,sınıf_bölümü,sınıf_mevcut)
    choice = input("Lütfen yapmak istediğiniz işlemi seçiniz : \n 1-SINIF BİLGİLERİ\n 2-Branş Değiştir\n 3-Çıkış Yap \n")

    if choice =='1':
        sınıf_oluştur.bilgileri_göster()
    elif choice =='2':
        sınıf_oluştur.branş_değiş()
    elif choice =='3':
        break
    else:
        print("Yanlış seçim yaptınız...")


   
    
