try:
    sayi1 = int(input("Lütfen 1. sayiyi giriniz : "))
    sayi2 = int(input("Lütfen 2. sayiyi giriniz : "))

    toplam = sayi1 / sayi2
    print(toplam)
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez...")

except ValueError:
    print("İstenen veri türünde bir değer giriniz lütfen...")

