def alan(r,pi = 3.14):
    return pi*r**2

alan1 = alan(6)
alan2 = alan(8)
print(alan2)
print(alan1)
print(alan1 + alan2)

def kimlik(isim = "bos" , soyisim = "bos", yas = "bos", tc = "bos"):
    print("Ad = ",isim ,"Soyisim",soyisim ,"Yaş = ",yas, "TC no = ", tc)

kimlik("Gokhan","akgun",22,5456465456546)

kimlik(yas=25,tc=855564655465)

def topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam
t = topla(54,45654,546,45,45,546,456,454,5546,64,45,123,8,4,666,77,8,2215,9,4848,54,8,989,856,65989,65)
print("toplam = ", t)

def isim(*args):
    print("{}  mekatronik mühendisi".format(args[0]))

isim(input("isim soyisim gir"))

def kimlik2(**kwargs):
    for key, value in kwargs.items():
        print("anahtarlar : ", key, "değerler :", value)

kimlik2(isim = "gokhan", soyisim = "akgun")

def birleştir(**kwargs):
    son = ""
    for kelimeler in kwargs.values():
        son += kelimeler
    return son

print(birleştir(a = "Python ", b = "Dünyanın en çok ", c = "kullanılan ", d = "dilidir."))

x = 10
print(x)

def kume():
    x = 5
    print(x)

x = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x:(x%2 == 0), x)))

print(list(map(lambda x:x**2, x)))

print(bin(5))
print(abs(-7.5))
print(max(x))
print(min(x))

print(pow(2,5,10))

y = reversed(x)
print(list(y))


print(round(5.18))
x = [10,8,52,77,25,878,6,88,12,36,7]

sorted(x)

print(sum(x))

class Tanim:
    isim = "gokhan"
    soyisim = "akgun"
    yas = 22
    not_ort = 85

bir = Tanim()

print(bir.isim)
print(bir.soyisim)
print(bir.yas)

class Ogrenci():
    def __init__(self,isim,soyisim,yas,not_ort):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.not_ort = not_ort

    def info(self):
        print("{} {} {} yaşında ve {} ortalamaya sahiptir.".format(self.isim,self.soyisim,self.yas,self.not_ort))

bir = Ogrenci("gokhan", "akgun", 22, 85)
iki = Ogrenci("ahmet", "saygı", 25, 95)
uc = Ogrenci("emir", "alp", 18, 70)

print(bir.soyisim)

bir.info()
iki.info()
uc.info()

class Ogretmen():
    def __init__(self,isim,soyisim,yas,maas,uzmanlik):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.__maas = maas
        self.uzmanlik = uzmanlik

    def info(self):
        print("{} {} {} yaşında {} TL maaşa sahip {} öğretmenidir.".format(self.isim,self.soyisim,self.yas,self.__maas,self.uzmanlik))

    def zam(self):
        return self.__maas * 1.3
    def getMaas(self):
        return self.__maas
    def setMaas(self, YeniMaas):
        YeniMaas = self.__maas


ali = Ogretmen("ali", "ince", 45, 5000, "fizik")

ali.info()
print(ali.zam())

print(ali.getMaas())