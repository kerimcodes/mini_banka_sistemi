import os

KLASOR = os.path.dirname(__file__)
veri_yolu = os.path.join(KLASOR,"veri.txt")

def kullanici_kayit():
    if not os.path.exists(veri_yolu):
        with open(veri_yolu,"a",encoding="utf-8"):
            pass


    while True:
        kullanici_adi = input("Bir kullanıcı adı seçiniz:")
        with open(veri_yolu,"r",encoding="utf-8") as okunacak:
            dosyalar = okunacak.readlines()
            isimler = [satir.strip().split("-")[0] for satir in dosyalar]
            if kullanici_adi in isimler:
                print("Bu kullanı adı daha önce seçilmiş,lütfen başka bir kullanıcı adı seçiniz.")
            else:
                break

    while True:        
        sifre = input("Lütfen kendinize 4 haneli sadace sayıdan oluşan bir şifre belirleyiniz")
        bakiye = 0
        if  sifre.isdigit() and len(sifre) == 4:
            with open(veri_yolu,"a",encoding="utf-8") as yaziliacak:
                yaziliacak.write(f"{kullanici_adi}-{sifre}-{bakiye}\n")
                print(f"Hesabınız kaydedildi {kullanici_adi}")
                break
        else:
            print("Şifre kriterleri karşılamıyor")

def kullanici_girisi():
    if not os.path.exists(veri_yolu):
        print("Henüz hiç veri yok")
        return None

    while True:
        kullanici_adi = input("Kullanıcı adınızı giriniz:")
        kullanici_sifre = input("Şifrenizi giriniz:")
        with open(veri_yolu,"r",encoding="utf-8") as okunacak:
            veriler = okunacak.readlines()
            for veri in veriler:
                ad,sifre,bakiye = veri.strip().split("-")
                if ad == kullanici_adi and sifre == kullanici_sifre:
                    return ad,bakiye
                
        print("Kullanıcı adı veya şifreniz hatalı")