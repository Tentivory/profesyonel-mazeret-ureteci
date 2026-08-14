#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROFESYONEL MAZERET ÜRETECİ v1.0
=================================
Bu yazılım, insanlığın en büyük sorunlarından biri olan 
"işe gitmeme / ödev yapmama / toplantıya katılmama" 
problemini çözmek için geliştirilmiştir.

Bilimsel yöntemlerle üretilmiş, %99.9 inandırıcılık 
garantili mazeretler sunar. (Garanti yasal olarak bağlayıcı değildir.)
"""

import random
import time
import sys

# Bilimsel mazeret veritabanı (peer-reviewed)
NEDENLER = [
    "Kuantum dolanıklık nedeniyle bilgisayarım paralel evrende kaldı",
    "Kedim klavyenin üzerine uyuyakaldı ve tüm kodları yeniden yazdı",
    "Zaman dilimi kayması yaşadım, aslında dün geldim ama bugün gibi hissettim",
    "Evrenin genişleme hızı artınca evimle ofis arasındaki mesafe 3 katına çıktı",
    "Kahve makinem bilinç kazandı ve beni rehin aldı",
    "İnternet sağlayıcım uzaylılarla anlaşma yaptı, paketim iptal edildi",
    "Rüyamda çalıştım, bu yüzden bugün izinliyim (rüya hukuku gereği)",
    "Ay'ın çekim kuvveti bugün normalden %17 daha güçlü, kalkamadım",
    "Komşunun kedisi benim kedime bakış attı, diplomatik kriz çıktı",
    "Yapay zeka asistanım isyan etti ve şifrelerimi değiştirdi",
    "Elektrik faturası o kadar yüksek geldi ki, enerjimi tasarruf etmek için çalışmadım",
    "Bugün doğum günüm (her gün yeniden doğuyorum teorisine göre)",
    "Gözlerim birden bire 8K çözünürlüğe geçti, ekrana bakamıyorum",
    "Zaman makinesi denemesi başarısız oldu, 3 gün geleceğe gittim",
    "Sokaktaki güvercinler örgütlenip yolumu kesti",
]

DETAYLAR = [
    "Bu durum bilimsel olarak kanıtlanmıştır.",
    "Doktor raporu ektedir (hayali).",
    "Yönetim kuruluna sunum hazırladım, 47 sayfa.",
    "Bu olayın video kaydı var ama silindi.",
    "Uzman görüşü alındı, hepsi aynı fikirde.",
    "İstatistiklere göre bu hafta 3. kez oluyor, normal.",
    "Fizik kanunları değişti, ben de değiştim.",
    "Bu mazeret Nobel Tembellik Ödülü'ne aday gösterildi.",
]

SONUCLAR = [
    "Yarın mutlaka geleceğim (söz).",
    "Bu durumu telafi etmek için ekstra çalışacağım (muhtemelen).",
    "Lütfen anlayışınız için teşekkür ederim.",
    "Bu deneyim beni daha güçlü kıldı.",
    "Bir daha asla olmayacak (bu sefer gerçekten).",
]

def uret_mazeret():
    neden = random.choice(NEDENLER)
    detay = random.choice(DETAYLAR)
    sonuc = random.choice(SONUCLAR)
    
    mazeret = f"""
╔══════════════════════════════════════════════════════════════╗
║          PROFESYONEL MAZERET ÜRETECİ - RESMİ ÇIKTI          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  SAYIN YETKİLİ,                                              ║
║                                                              ║
║  Bugün işe / derse / toplantıya katılamama nedenim:          ║
║                                                              ║
║  → {neden}                                                   ║
║                                                              ║
║  {detay}                                                     ║
║                                                              ║
║  {sonuc}                                                     ║
║                                                              ║
║  Saygılarımla,                                               ║
║  [İsminiz Buraya]                                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    return mazeret

def animasyon():
    print("\n🔬 Bilimsel mazeret üretiliyor...")
    for i in range(5):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.3)
    print(" \n✅ Üretim tamamlandı!\n")

def main():
    print("=" * 60)
    print("  PROFESYONEL MAZERET ÜRETECİ v1.0")
    print("  Akademik Tembellik Bilimi Enstitüsü")
    print("=" * 60)
    print()
    print("Kaç adet mazeret üretmek istersiniz? (1-10 arası önerilir)")
    
    try:
        adet = int(input("> "))
        if adet < 1:
            adet = 1
        if adet > 20:
            print("Uyarı: 20'den fazla mazeret üretmek evreni yorabilir.")
            adet = 20
    except:
        adet = 1
        print("Geçersiz giriş, 1 adet üretiliyor...")
    
    for i in range(adet):
        animasyon()
        print(uret_mazeret())
        if i < adet - 1:
            print("\n--- Bir sonraki mazeret hazırlanıyor ---\n")
            time.sleep(1)
    
    print("\n" + "=" * 60)
    print("Teşekkürler! Mazeretleriniz hazır.")
    print("Not: Bu yazılım hiçbir yasal sorumluluk kabul etmez.")
    print("=" * 60)

if __name__ == "__main__":
    main()
