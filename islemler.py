from datetime import datetime
import os 

KLASOR = os.path.dirname(__file__)
veri_yolu = os.path.join(KLASOR,"veri.txt")



def dosya_guncelle(kullanici_adi, yeni_bakiye):
    with open(veri_yolu, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    with open(veri_yolu, "w", encoding="utf-8") as f:
        for satir in satirlar:
            ad, sifre, bakiye = satir.strip().split("-")
            if ad == kullanici_adi:
                f.write(f"{ad}-{sifre}-{yeni_bakiye}\n")
            else:
                f.write(satir)

def para_islemleri(kulllanici_adi,mevcut_bakiye):
    islem_yolu = os.path.join(KLASOR,f"{kulllanici_adi},gecmis.txt")
    mevcut_bakiye = int(mevcut_bakiye)

    while True:   
        print("1- Para Yatır")
        print("2- Para Çek")
        print("3- Bakiye Görüntüle")
        print("4- İşlem Geçmişini Görüntüle")
        print("5- Çık")
        secim = input("Seçiminiz:")
        if secim == "1":
            miktar = input("Yatırılacak tutarı giriniz:")
            if not miktar.isdigit():
                print("Lütfen sayı ile yazınız.")
                continue
            miktar = int(miktar)
            mevcut_bakiye += miktar

            dosya_guncelle(kulllanici_adi,mevcut_bakiye)

            with open(islem_yolu,"a",encoding="utf-8") as yazilacak:
                yazilacak.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M")} tarihinde {miktar} TL tutarında para yatırıldı.\n")
                    
        elif secim == "2":
            miktar = input("Çekmek istediğiniz tutarı giriniz:")
            if not miktar.isdigit():
                print("Lütfen tutarı sayı ile giriniz")
                continue
            miktar = int(miktar)
            if miktar > mevcut_bakiye:
                print("Yetersiz Bakiye")
                continue
            mevcut_bakiye -= miktar

            dosya_guncelle(kulllanici_adi,mevcut_bakiye)

            with open(islem_yolu,"a",encoding="utf-8") as yazilacak:
                yazilacak.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M")} tarihinde {miktar} TL tutarında para çekildi.\n")
                    
        elif secim == "3":
                with open("veri.txt","r",encoding="utf-8") as okunacak:
                    veriler = okunacak.readlines()
                    for veri in veriler:
                        ad,sifre,bakiye = veri.strip().split("-")
                        if ad == kulllanici_adi:
                            print(f"Mevcut bakiyeniz: {bakiye}")
                            
        elif secim == "4":
            try:
                with open(f"{kulllanici_adi}.gecmis.txt","r",encoding="utf-8") as okunacak:
                    islemler = okunacak.readlines()
                    for i,islem in enumerate(islemler,start=1):
                        print(f"{i}-{islem}")
            except FileNotFoundError:
                print("İşlem geçmişi bulunmamaktadır.")

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Hatalı seçim")
