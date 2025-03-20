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

class müdür(okul):
    print("***Yönetici Paneli***")
    def __init__(self, şube, öğretmen, bölüm, mevcut,kıdem):
        
        super().__init__(şube,öğretmen,bölüm,mevcut)
        self.kıdem=kıdem
        
        '''
        self.şube=şube
        self.öğretmen=öğretmen
        self.bölüm=bölüm
        self.mevcut=mevcut
        self.kıdem = kıdem
        '''

    def bilgileri_göster(self):
        print("-"*45)
        print("SINIF BİLGİLERİ : ")
        şube=input("Lütfen şubeyi giriniz :")
        öğretmen =input("Lütfen öğretmenin ismini giriniz :")
        bölüm = input("Lütfen bölümü giriniz :")
        mevcut =int(input("Lütfen mevcutu giriniz : "))
        kıdem = input("Lütfen kıdemi giriniz :")
        print("-"*45)
        print("^"*50)
        print("ŞUBE : {}\nÖĞRETMEN : {}\nBÖLÜM : {}\nMEVCUT : {}\nKIDEM : {}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut,self.kıdem))
        print("^"*50)




yönetici = müdür("YAZILIM 3","BARIŞ YASİN ŞAHİN","YAZILIM",95,"BÖLÜM TEMSİLCİSİ")
yönetici.bilgileri_göster()


