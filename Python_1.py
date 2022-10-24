isim = "gökhan"

print("selam\nben {}\nyaşım {}".format('gökhan', 21))
print("\n")
print("merhaba ben {ad} ve benim yaşım {yas}".format(ad='gokhan', yas=21))
print("\n")
print("selam\nben {}\nyaşım {}".format(isim, 21))
print("\n")

sayi = 10
print(sayi)

sayi = sayi + 1
print(sayi)
sayi = 0

sayyi = 15*2/3
sayi2 = 15.2/3.7
print("sayi 1 {s1}\nsayi 2 {s2}".format(s1 = sayyi , s2 =sayi2))

stvar = "gökhan"
stvar2 = stvar + " pyton"
print(stvar2,"\n")

a = True
b = 'False'
c = False
print(a)
print(b)
print(type(b))
print(type(c),"\n")

yas1 = 17
yas2 = 21
print("yas 2 büyk mü ",yas2 > 18)
print("yas 1 büyük mü ",yas1 > 18,"\n")
if(yas1 >= 18):
    print("yas 1",True)
else:
    print("yas 1",False)
if(yas2 >= 18):
    print("yas 2",True,"\n")
else:
    print("yas 2",False,"\n")

Liste = ['a','b','c']
hedef_harf = 'd'

if hedef_harf in Liste:
    print("{} burada\n".format(hedef_harf))
else:
    print("{} burada deil".format(hedef_harf))
    Liste.append("d")
    print("Listeye ekledim\nGüncel liste =", Liste,"\n")

ad = input('Adınızı girin = ')
yas = input('Yaşınızı girin = ')

print("adınız = {}\nYaşınız = {}".format(ad , yas))

sayi3 = input("girilen sayının tek yada çift olduğunu algılama sayi girin = ")
sayi4 = 1

if (int(sayi3) % 2 == 0):
    print("sayı çift")
else:
    print("sai tek")
kullanici_sayisi = 0
kullanicilar = ["Ahmet Oksüz", "Mehmet Candan","Gökhan Akgün","Burak Kılıç","Engin Gönenc"]

for kullanici in kullanicilar:
    kullanici_sayisi += 1
    ad , soyad = kullanici.split()[0], kullanici.split()[1]
    print("{} kullanıcı adı {} kullanıcının soyadı {}".format(kullanici_sayisi,ad,soyad))

x = 0
while(x < 10):
    print("{} değeri 10 dan küçüktür".format(x))
    x += 1

list2 = range(10)
print(list2)

print("range = {}".format(list2))

for sayi4 in range(11):
    print(sayi4)

harfler = ["a","b","c","d","e"]
for harf in harfler:
    print(harf)

for harf in enumerate(harfler):
    print(harf)

for index , harf in enumerate(harfler):
    print(index , harf)

for index , harf in enumerate(harfler):
    print("{}. harf:{}".format(index+1, harf))

ulkeler = ["TR","FR","EN","DE"]
siralamalar = range(1,5)

for ulke in zip(siralamalar, ulkeler):
    print(ulke)

def sayilar():
    print("5")
    yaz = range(10)
    print(yaz)
def sayi_dondur(a,b):
    if(a>b):
        #print(a)
        return a

    elif(b>a):
        #print(b)
        return b

print("kod başladı")
sayilar()

#sayi_dondur(28,5)

print(sayi_dondur(2,39))
print(sayi_dondur(28,3))

kume.add(91)
print(kume)
kume.discard(99)
print(kume)
kume.remove(22)
print(kume)
kume2 = {22,35,64,75,16,28,2,5,6,8,9}
kume.update(kume2)
print(kume)

a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4,5,688,41,22,12}
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
print(a.union(b))

print(len(a))
c = 5.8
print(c)
print(type(c))
print(int(c))

list2 = range(10)
print(list2)

print("range = {}".format(list2))

for sayi4 in range(11):
    print(sayi4)

harfler = ["a","b","c","d","e"]
for harf in harfler:
    print(harf)

for harf in enumerate(harfler):
    print(harf)

for index , harf in enumerate(harfler):
    print(index , harf)

for index , harf in enumerate(harfler):
    print("{}. harf:{}".format(index+1, harf))

ulkeler = ["TR","FR","EN","DE"]
siralamalar = range(1,5)

for ulke in zip(siralamalar, ulkeler):
    print(ulke)


