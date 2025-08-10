# #Verilen String İfadenin Hepsini Bu Şekilde Dolanabilirsin
# isim = "Ahmet"
# for i in isim:
#     print(i)
# #-----------------------------------------------------------
# myTuple = [(2,4),(3,5),(7,9)]
# for x in myTuple:
#     print(x)
# for y,z in myTuple:
#     print(y,z)

# myDict = {"41": "Kocaeli", "55": "Samsun", "35": "İzmir"}
# for n in myDict: #istesen myDict.keys() diyebilirsin
#     print(n) #bu verirsen sadece sayıları yazdırır.

# for m in myDict: #bunun yerine myDict.values() diyerek işim içinden çıkabilirsin
#     print(myDict[m]) 

# for t,r in myDict.items(): #key ve valu degerlerini birlite yazdırır.
#     print(t,r)


sayilar = [3,5,7,2,12,32,45]
x = []
for i in sayilar:
    if i % 3 == 0:
        x.append(i)

print(x)

urunler = ["iphone 11", "samsun s22", "iphone 12", "redmi 14", "iphone 15"]

for x in urunler:
    index = x.find('iphone')
    if index > -1:
        print(x)
