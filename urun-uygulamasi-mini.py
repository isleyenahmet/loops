urunler= [
    {"urunAdi":"HP Victus", "fiyat":32999},
    {"urunAdi":"Lonovo ThinkPad", "fiyat":25999},
    {"urunAdi":"Apple Macbook", "fiyat":49999},
    {"urunAdi":"Huawei Matebook", "fiyat":26999},
    {"urunAdi":"Casper Nirvana", "fiyat":20000}
]

# #İstenilen: Örnek cümleyi tüm ürünlere uygula:
# #Hp Victus marka ürünün fiyati 32999 türk lirasıdır.
# for x in urunler:
#     print(f"{x['urunAdi']} marka ürünün fiyati {x['fiyat']} türk lirasidir.")

# #urunler fiyatlarının toplamı nedir?
# toplam = 0
# for y in urunler:
#     toplam += y["fiyat"]
# print(toplam) 

# #25000 ile 40000 TL arasindaki ürünleri listeleyiniz
# aralik = []
# for i in urunler:
#     if i["fiyat"] > 25000 and i["fiyat"] < 40000:
#         aralik.append(i)
# print(aralik)

#Kullanicidan alınan Key değerlerine göre ürünleri listeleyiniz:

kelime = input("Hangi Cihazin Ücretini Öğrenmek İstiyorsunuz: ")
for i in urunler:
    try:
        if (i["urunAdi"].lower().find(kelime.lower())) > -1: #çok önemli bir nokta arananı da arayacağımızı da küçük harf yaptık
            print(f"{i["urunAdi"]} urununun fiyati {i["fiyat"]}TL dir")
            break
    except (ValueError,TypeError) as e:
        print(e)
