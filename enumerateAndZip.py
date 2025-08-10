#ENUMERATE
# arabalar = ["bmw", "audi", "opel"]

# obj1 = enumerate(arabalar,1) #oradaki 1 sayının başlangıç değeri
# print(list(obj1))

# for index,marka in enumerate(arabalar,1):
#     print(f"{index}-{marka}")


#ZİP birleştirme işlemi
isim = ["Ahmet", "Mehmet", "Selim"]
numara = [100,200,300]
print(list(zip(numara,isim)))

for i,j in zip(numara,isim): #yukarıdaki işlemin aynısı da liste methodu ile yapmış olduk
    print(f"{i}-{j}")