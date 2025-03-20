class galeri:
    arac_ismi = "Ferrari"
    km_degeri = 3000
    renk = "Kırmızı"

    def araba_özellikleri(self):
        print(f"Araç İsmi : {self.arac_ismi}\n")
        print(f"Aracın rengi : {self.renk}\n")
        print(f"Aracın kilometre bilgisi :{self.km_degeri}\n")

baris_otomativ = galeri()
baris_otomativ.araba_özellikleri()
