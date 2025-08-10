#range kullanımı diğer dillerde biraz karmaşık olsa da python da çok kolay
# Örnek C++:
# for int i = 0 ; i < 100 ; i++

toplam = 0
for i in range(0,100,2):
    toplam += i

print(toplam)

#işin mantığını kavramak için range aslında bir liste oluşturur:
rng = range(10) # bu bize 0 dan 10 dahil olmadan olan sayıları liste olarak tutar
rng2 = range(10,20) #10 dan 20 ye 20 dahil olmadan ilerle
rng3 = range(10,20,2) #10 dan 20 ye ikişer art
sonuc = list(rng)
print(sonuc) #gibi