from kullanici import kullanici_girisi,kullanici_kayit
from islemler import para_islemleri
while True:
    print("1- Kayıt Ol")
    print("2- Giriş Yap")
    print("3- Çık")
    secim = input("Seçiminiz:")

    if secim == "1":
        kullanici_kayit()

    elif secim == "2":
        sonuc = kullanici_girisi()
        if sonuc is None:
            continue

        kullanici,bakiye = sonuc
        para_islemleri(kullanici,bakiye)
    
    elif secim == "3":
        print("Çıkış yapılıyor")
        break
    
    else:
        print("Hatalı seçim")