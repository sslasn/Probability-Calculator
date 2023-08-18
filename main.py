#olasılık hesabı
import random
# Renk sınıfları ve topların dağılımı
renk_siniflari = ['Kirmizi', 'Mavi', 'Yesil']
toplar = ['Kirmizi', 'Mavi', 'Yesil', 'Mavi']

# Top çekilişi ve renk seçimi
cekilen_top = random.choice(toplar)

# Renk seçimine göre olasılığı hesapla
renk_sayisi = len(renk_siniflari)
top_sayisi = len(toplar)
renk_sayisi_cikar = toplar.count(cekilen_top)

olasilik = renk_sayisi_cikar / top_sayisi

print(f"Çekilen top: {cekilen_top}")
print(f"Renk seçilmesi olasılığı: {olasilik:.2f}")