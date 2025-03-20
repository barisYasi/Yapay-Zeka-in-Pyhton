class okul:
    def __init__(self,sınıf,bölüm,öğretmen,mevcud):
        self.sınıf = sınıf
        self.bölüm=bölüm
        self.öğretmen = öğretmen
        self.mevcud=mevcud
        
    
    def bilgileri_göster(self):
        print("-"*45)
        print("SINIF BİLGİLERİ:")
        print("Sınıf : {}\nBölüm : {} \nÖğretmen : {}\nMevcud : {} ".format(self.sınıf,self.bölüm,self.öğretmen,self.mevcud))
        print("-"*45)

birinci_sınıf = okul("İSTÜN-1","Diş Ve Çene Cerrahisi","BERAT ŞENDUL",30)
birinci_sınıf.bilgileri_göster()

ikinci_sınıf = okul("İSTÜN-2","ENDODONTİ","ENES TEKİN",25)
ikinci_sınıf.bilgileri_göster()