import time
try:
    sayi1 = int(input("Lütfen 1. sayıyı giriniz.:"))
    sayi2 = int(input("Lütfen 2. sayıyı giriniz :"))
    sonuc = sayi1+sayi2
    print(sonuc)

except ValueError:
    print("Lütfen istenilen değeri gir koçum...")

finally:
    sayac = 5
    for i in range(5):
        time.sleep(1)
        print("Geri sayım :",sayac)
        sayac -= 1
print("İşlem tamamlandı")

