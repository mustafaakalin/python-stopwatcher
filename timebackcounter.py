import os
import time
import datetime



# Kullanıcıdan saat, dakika ve saniye değerlerini al
saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))

# Toplam saniye değerini hesapla
toplam_saniye = saat * 3600 + dakika * 60 + saniye

while toplam_saniye:
    # Terminal ekranını temizle
    os.system('cls' if os.name == 'nt' else 'clear')

    # Yıl, Ay, Hafta, Gün ,Saat, dakika ve saniye formatına çevir
    saat = toplam_saniye // 3600
    toplam_saniye %= 3600
    dakika = toplam_saniye // 60
    toplam_saniye %= 60


    print("TODAY DATETIME:" , datetime.datetime.now().ctime())
    
    print(f"\n\n\n\nTIME REMAINING:              \n\n{saat:02} Hours {dakika:02} minute {toplam_saniye:02} Second Left")

    time.sleep(1)
    toplam_saniye -= 1

# Terminal ekranını temizle
os.system('cls' if os.name == 'nt' else 'clear')

# "ZAMAN DOLDU" mesajını yazdır
print("ZAMAN DOLDU")