import subprocess

psw ="015634"
kullanıcı_sifre =input("Lütfen şifreyi giriniz ")

if kullanıcı_sifre == psw:
     while True:
        print("**** SEÇİM EKRANINA HOŞGELDİNİZ ***")

        seçim_yap = input("1-Notepad\n  2-Hesap Makinası\n")
        
        if seçim_yap == "1":
            subprocess.call("notepad.exe")
            seçim=input("Devam edilsin mi ? E/H    :   ")
            if seçim != "e":
                break
    
        elif seçim_yap == "2":
            subprocess.call("calc.exe")
            seçim = input("Devam edilsin mi ? E/H  :    ")
            if seçim != "e":
                break
                    
        else:
            print("Hatalı seçim yaptınız efendim...")
            break

else:
    print("Şifre yanlış bro")
