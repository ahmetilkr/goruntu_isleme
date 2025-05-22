"""class Ogrenci:
  def __init__(self, ad, yas):
    self.ad = ad
    self.yas = yas
  def bilgi_ver(self):
    print("öğrencinin adı:{},öğrencinin yaşı:{}".format(self.ad,self.yas))
ogr=Ogrenci("Ali",20)
ogr.bilgi_ver()"""
from pygments.lexer import words

#*****************************************************************
"""class Kitap:
  def __init__(self,ad,yazar):
    self.ad=ad
    self.yazar=yazar
  def ekrana_yaz(self):
    print("kitabın adı:{},kitabın yazarı:{}".format(self.ad, self.yazar))
kitap_n=Kitap("1984","George Orwell")
kitap_n.ekrana_yaz()
kitap_n=Kitap("küçük prens","Antoine de Saint-Exupéry")
kitap_n.ekrana_yaz()"""
#*********************************************************
"""class Araba:
  
"""
#*************************************************************
#Bir kütüphane yönetim sistemi geliştirmek istiyorsunuz. Her kitabın adı, yazarı ve mevcut adet sayısı tutulmalı.
#Kullanıcılar kitap ödünç alabilecek ve kitap iade edebilecekler. Her işlem sonucunda kitap adedi güncellenmeli
#Eğer ödünç alınmak istenen kitap yoksa kullanıcıya bunun mümkün olmadığı söylenmeli.
"""
class Kütüphane:
  def __init__(self,ad,yazar,adet):
    self.ad=ad
    self.yazar=yazar
    self.adet=adet
class Kitap:
  Kitaplar=[]
  def kitap_ekle(self,kitap):
    Kitap.Kitaplar.append(kitap)
  def kitap_ara(self,aranan):

    for i in Kitap.Kitaplar:
      if i.ad==aranan:
        print("aradığınız kitap bulundu")
        x=i.adet
        print("kalan adet sayısı{}".format(x-1))
        break
      else:
        print("aradığınız kitap bulunamadı")
k1=Kütüphane("1984","George Orwell",5)
k2=Kütüphane("küçük prens","Antoine de Saint-Exupéry",3)
book=Kitap()
book.kitap_ekle(k1)
book.kitap_ekle(k2)
aranan_kitap=input("aranacak kitabı giriniz")
book.kitap_ara(aranan_kitap)
"""
#******************************************************
"""Bir otomobil servis sistemi tasarlıyorsunuz. Her arabanın markası, modeli ve kilometresi olmalı.
Kullanıcı arabasını servise getirdiğinde kilometresi güncellenmeli ve bu bilgiyi takip edebilmelisiniz.
Ayrıca, servise giren arabaların kaydını tutmalı ve bu kayıtları listeleyebilmelisiniz. (2 sınıf oluşturunuz)"""
"""
class Otomobil:
  def __init__(self,marka,model,km):
    self.marka=marka
    self.model=model
    self.km=km

class takip:
  k_arabalar=[]
  def kayıt(self,nesne):
    takip.k_arabalar.append(nesne)
    print("{} listeye kaydedildi".format(nesne.marka))
  def g_araba(self,seçim_par):
    print("{} servise getirildi,güncel kilometre:{}".format(seçim_par.marka,seçim_par.km))
  def tüm_arabalar(self):
    for i in takip.k_arabalar:
      print("marka:{},model:{},km:{}".format(i.marka,i.model,i.km))

o1=Otomobil("toyota","2020","10000")
o2=Otomobil("ford","2024","20000")
takip_n=takip()
takip_n.kayıt(o1)
takip_n.kayıt(o2)
seçim=int((input("hangi arabayı servise götürmek istersiniz?""1-->toyota,2--->ford")))
if(seçim==1):
  takip_n.g_araba(o1)
if (seçim == 2):
  takip_n.g_araba(o1)
takip_n.tüm_arabalar()
"""
#***********************************************************************
#Bir bankada hesap yönetim sistemi oluşturuyorsunuz. Her kullanıcının bir hesabı olacak ve hesap bakiyesi tutulacak.
#Kullanıcı para yatırabilecek ve para çekebilecek
#Eğer kullanıcı bakiyesinden fazla para çekmeye çalışırsa, sistem buna izin vermemeli ve kullanıcıyı uyarmalı.
"""
class Kullanıcı:
  def __init__(self,ad,bakiye):
    self.ad=ad
    self.bakiye=bakiye
class İşlemler:
  def paracekme(self,kullanıcı,girilen):
    return kullanıcı.bakiye-girilen
  def parayatırma(self,kullanıcı,girilen):
    return kullanıcı.bakiye+girilen
k1=Kullanıcı("ahmet",15000)
seçim=int(input("1--->para çekme,2-->para yatırma"))
işlem=İşlemler()
if seçim==1:
  ç_tutar=int(input("çekmek istediğiniz tutarı giriniz"))
  x=işlem.paracekme(k1,ç_tutar)
  print(x)
elif seçim==2:
  y_tutar = int(input("yatırmak istediğiniz tutarı giriniz"))
  x=işlem.parayatırma(k1,y_tutar)
  print(x)
"""
#********************************************************************
"""Bir online alışveriş sistemi için bir sepet yönetim sistemi tasarlıyorsunuz
Kullanıcı, sepete ürün ekleyebilecek ve sepetindeki ürünleri listeleyebilecek. Her ürünün adı, fiyatı ve adedi tutulacak.
Kullanıcı toplam tutarı görebilmeli. (2 sınıf oluşturunuz)"""
"""
class Ürünler:
  def __init__(self,ad,fiyat):
    self.ad=ad
    self.fiyat=fiyat

class Sepet:
  def __init__(self):
    self.Sepetim = []
    self.toplam_fiyat = 0

  def ürün_ekle(self,nesne,g_adet):
    self.Sepetim.append((nesne,g_adet))
    self.toplam_fiyat+=g_adet*nesne.fiyat
  def sepet_ücreti(self):
    print("sepet ücretinizi{}".format(self.toplam_fiyat))
  def sepet_göster(self):
    for ürün,adet in self.Sepetim:
      print("- {}, Adet: {}, Fiyat: {} TL".format(ürün.ad, adet, ürün.fiyat))
      
ü1=Ürünler("kulaklık",2000)
ü2=Ürünler("pc",40000)
ü3=Ürünler("mouse",3000)
ü4=Sepet()
while True:
 seçim=int(input("eklemek istediğiniz ürünü seçiniz:1--->kulaklık,2-->pc,3-->mouse,sepeti gçrüntüülemek için 4 e,çıkmak için 5 e basınız"))
 if seçim==4:
   ü4.sepet_göster()
   ü4.sepet_ücreti()
   continue
 if seçim == 5:
   break
 seçim_adeti=int(input("seçtiğiniz üründen kaç adet eklemek istersiniz"))
 if seçim==1:
  ü4.ürün_ekle(ü1,seçim_adeti)
 if seçim==2:
   ü4.ürün_ekle(ü2,seçim_adeti)
 if seçim ==3:
   ü4.ürün_ekle(ü3,seçim_adeti)
"""
#*******************    SINAV **************************************
#Bir Calisan sınıfı oluşturun. Bu sınıfın her çalışan için ad, soyad ve maaş bilgilerini tutmasını sağlayın
#Ayrıca, maaşı yüzde belirli bir oranda artırmak için maas_artir adında bir fonksiyon oluşturun.
#Ali Kaya maaşı güncellendi: 5500.0 TL
"""
class calisan():
  def __init__(self,ad,soyad,maas):
   self.ad=ad
   self.soyad=soyad
   self.maas=maas
  def maas_artir(self):
    self.maas += self.maas * 10 / 100
  def maas_yaz(self):
      print("{}nın yeni maaşı güncellendi,gncel maas:{}".format(self.ad, self.maas))
c1=calisan("ahmet","kahraman",100000)
c2=calisan("ferdi","tayfur",300000)
print("kullanıcılar:1-->ahmet,2-->ferdi")
seçim=int(input("maaşını arttırmak istediğiniz kullanıcıyı giriniz"))
if seçim==1:
  c1.maas_artir()
  c1.maas_yaz()
if seçim==2:
  c2.maas_artir()
  c2.maas_yaz()
"""
#Bir alışveriş sepeti uygulaması için Urun ve Sepet adında iki sınıf tanımlayın.
#Urun sınıfı, ürün adı ve fiyatını içermelidir.
#Sepet sınıfı ise, sepete ürün eklemeli ve toplam tutarı hesaplamalıdır.
#Kitap sepete eklendi.
#Kalem sepete eklendi.
#Toplam tutar: 35 TL
#***********************************************************************
"""
# Bir Calisan sınıfı oluşturun. Bu sınıfın her çalışan için ad, soyad ve maaş bilgilerini tutmasını sağlayın
#Ayrıca, maaşı yüzde belirli bir oranda artırmak için maas_artir adında bir fonksiyon oluşturun.
class calisan():
  def __init__(self,ad,soyad,maas):
   self.ad=ad
   self.soyad=soyad
   self.maas=maas
  def maas_artir(self):
    self.maas += self.maas * 10 / 100
  def maas_yaz(self):
      print("{}nın yeni maaşı güncellendi,gncel maas:{}".format(self.ad, self.maas))
c1=calisan("ahmet","kahraman",100000)
c2=calisan("ferdi","tayfur",300000)
print("kullanıcılar:1-->ahmet,2-->ferdi")
seçim=int(input("maaşını arttırmak istediğiniz kullanıcıyı giriniz"))
if seçim==1:
  c1.maas_artir()
  c1.maas_yaz()
if seçim==2:
  c2.maas_artir()
  c2.maas_yaz()
"""
#***********************************************************************
"""
class ürün_adı:
  def __init__(self,ad,fiyat):
    self.ad=ad
    self.fiyat=fiyat
class sepet():
  Sepet=[]
  toplam_fiyat=0
  def ürün_ekle(self,nesne):
    sepet.Sepet.append(nesne.ad)
    sepet.toplam_fiyat +=nesne.fiyat
  def toplam_tutar(self):
    print("sepetin toplam tutarı:{}".format(sepet.toplam_fiyat))


a1=ürün_adı("kalem",15)
a2=ürün_adı("kitap",20)
s=sepet()
while True:
  print("sepete eklemek istediğiniz ürününler:1-->kalem,2-->kitap,3-->toplam tutar,4-->çıkış")
  seçim=int(input())
  if(seçim==1):
    s.ürün_ekle(a1)
  elif (seçim == 2):
    s.ürün_ekle(a2)
  elif (seçim == 3):
    s.toplam_tutar()
  elif seçim==4:
    break
  else:
        print("yanlış seçim yaptınız (1-4)seçim yapınız")
"""
#***********************************************************************
#Bir öğrenci yönetim sistemi için Ogrenci ve Ders adlı iki sınıf oluşturun.
# Ogrenci sınıfı, öğrenci adı ve numarasını içermeli
# Ders sınıfı, ders adı ve öğrenci listesini tutmalı, ogrenci_ekle fonksiyonuyla öğrenci ekleyebilmeli.
"""
ogrenci1 = Ogrenci("Ayşe", 101)
ogrenci2 = Ogrenci("Mehmet", 102)

ders = Ders("Matematik")
ders.ogrenci_ekle(ogrenci1)
ders.ogrenci_ekle(ogrenci2)
ders.ogrenci_listesi()
"""
"""
class ogrenci:
  def __init__(self,ad,numara):
    self.ad=ad
    self.numara=numara
class Ders:
  ogrenciler=[]
  def __init__(self,ders):
    self.ders=ders
  def ogrenci_ekle(self,nesne):
    Ders.ogrenciler.append(nesne)
    print("{} isimli {} numaralı öğrenci {} dersine eklendi".format(nesne.ad, nesne.numara, self.ders))
  def ogrenci_listesi(self):
    for ogrenci in Ders.ogrenciler:
      print("{}, {}".format(ogrenci.ad, ogrenci.numara))
ders = Ders("Matematik")
ogrenci1=ogrenci("ayşe",101)
ogrenci2=ogrenci("mehmet",102)
ders.ogrenci_ekle(ogrenci1)
ders.ogrenci_ekle(ogrenci2)
ders.ogrenci_listesi()

#*****************************************************************
# Bir otopark yönetim sistemi geliştirin. Arac sınıfı, aracın plakası ve marka bilgilerini içermelidir.
#Otopark sınıfı, park edilen araçları tutmalı, arac_park_et fonksiyonuyla araç park edebilmeli
#arac_listesi fonksiyonuyla park edilen araçları listeleyebilmelidir.
"""
"""
34ABC123 plakalı Toyota park edildi.
35XYZ789 plakalı Honda park edildi.
Park edilen araçlar:
- Plaka: 34ABC123, Marka: Toyota
- Plaka: 35XYZ789, Marka: Honda
"""
"""
class Arac:
  def __init__(self,plaka,marka):
    self.plaka=plaka
    self.marka=marka
class Otopark():
  araclar=[]
  def arac_parket(self,nesne):
    print("{} plakalı {} marka araç park edildi".format(nesne.plaka,nesne.marka))
    Otopark.araclar.append(nesne)
  def arac_listesi(self):
    for arac in Otopark.araclar:
      print("{}:plaka {}:marka".format(arac.plaka,arac.marka))
a1=Arac("34ABC123","Toyota")
a2=Arac("35XYZ789","Honda")
o1=Otopark()
o1.arac_parket(a1)
o1.arac_parket(a2)
o1.arac_listesi()
"""
#*****************************************************************
# Bir bankada hesap yönetim sistemi oluşturun. BankaHesabi sınıfı, hesap sahibinin adını ve bakiyesini tutmalı.
# para_yatir ve para_cek fonksiyonları ile hesap işlemlerini gerçekleştirin.
# Eğer bakiye yetersizse kullanıcıyı uyaran bir mesaj verin.
"""
class BankaHesabi:
  def __init__(self,ad,bakiye):
    self.ad=ad
    self.bakiye=bakiye
class İşlemler:
  def paracekme(self,kullanıcı,girilen):
    if kullanıcı.bakiye<girilen:
      return "bakiye yetersiz"
    else:
      return "yeni bakiyeniz {}:".format(kullanıcı.bakiye-girilen)
  def parayatırma(self,kullanıcı,girilen):
    return kullanıcı.bakiye+girilen
k1=BankaHesabi("Zeynep", 1000)
seçim=int(input("1--->para çekme,2-->para yatırma"))
işlem=İşlemler()
if seçim==1:
  ç_tutar=int(input("çekmek istediğiniz tutarı giriniz"))
  x=işlem.paracekme(k1,ç_tutar)
  print(x)
elif seçim==2:
  y_tutar = int(input("yatırmak istediğiniz tutarı giriniz"))
  x=işlem.parayatırma(k1,y_tutar)
  print(x)
"""
#*****************************************************************

#Bir kütüphane yönetim sistemi geliştirin.
#Bu sistemde, kitapları yönetmek ve üyelerin ödünç alıp verme işlemlerini
#takip etmek için Kitap ve Kutuphane adında iki sınıf oluşturun.
"""
Kitap sınıfı:

Kitabın adını ve mevcut stok miktarını tutmalıdır.
stok_guncelle adlı bir fonksiyonla stokları güncelleyebilmelidir.
Kutuphane sınıfı:

Birden fazla kitabı yönetmek için bir kitaplar listesi içermelidir.
kitap_ekle fonksiyonuyla kütüphaneye yeni bir kitap ekleyebilmelidir.
odunc_al fonksiyonuyla bir üyeye kitap ödünç vermelidir. Eğer kitap stokta yoksa, kullanıcıya uygun bir mesaj vermelidir.
geri_ver fonksiyonuyla ödünç alınan bir kitabı geri almalıdır.
stok_goruntule fonksiyonuyla kütüphanedeki kitapların mevcut stok durumunu listelemelidir.
"""
"""
class Kitap:
  def __init__(self,ad,yazar,adet):
    self.ad=ad
    self.yazar=yazar
    self.adet=adet
class Kütüphane:
  Kitaplar=[]
  def kitap_ekle(self,kitap):
    Kütüphane.Kitaplar.append(kitap)
  def odunc_al(self,aranan):

    for i in Kütüphane.Kitaplar:
      if i.ad==aranan:
        print("aradığınız kitap bulundu")
        i.adet=i.adet-1
        x=i.adet
        print("kalan adet sayısı{}".format(x))
        break
    else:
        print("aradığınız kitap bulunamadı")
  def geri_ver(self,verilen_kitap_p):
    for kitap in Kütüphane.Kitaplar:
      if kitap.ad == verilen_kitap_p:
        kitap.adet += 1
        print(f"{verilen_kitap_p} kitabı başarıyla geri verildi. Kalan adet: {kitap.adet}")
        break
    else:
        print(f"{verilen_kitap_p} kitabı kütüphanede bulunamadı.")
  def stok_goruntule(self):
    print("Kütüphanedeki Kitaplar ve Stok Durumu:")
    for kitap in Kütüphane.Kitaplar:
      print(f"Kitap: {kitap.ad}, Yazar: {kitap.yazar}, Stok Adedi: {kitap.adet}")


k1=Kitap("1984","George Orwell",5)
k2=Kitap("küçük prens","Antoine de Saint-Exupéry",3)
book=Kütüphane()
book.kitap_ekle(k1)
book.kitap_ekle(k2)
aranan_kitap=input("aranacak kitabı giriniz")
book.odunc_al(aranan_kitap)
verilen_kitap=input("verilecek kitabı giriniz")
book.geri_ver(verilen_kitap)
book.stok_goruntule()
"""

"""
class Ürün:
  def __init__(self, ad, fiyat, stok):
    self.ad = ad
    self.fiyat = fiyat
    self.stok = stok


class Sepet:
  def __init__(self):
    self.ürünler = []

  def ürün_ekle(self, ürün, miktar):
    if ürün.stok < miktar:
      print(f"Yetersiz stok: {ürün.ad}")
      return
    for item in self.ürünler:
      item_ürün, item_miktar = item
      if item_ürün == ürün:
        item[1] += miktar  # Miktarı artır
        ürün.stok -= miktar
        return
    self.ürünler.append([ürün, miktar])  # Yeni ürün ekle
    ürün.stok -= miktar

  def ürün_sil(self, ürün):
    for item in self.ürünler:
      item_ürün, item_miktar = item
      if item_ürün == ürün:
        self.ürünler.remove(item)  # Ürünü listeden çıkart
        ürün.stok += item_miktar
        return
    print(f"{ürün.ad} sepette yok.")

  def toplam_fiyat(self):
    toplam = 0
    for item in self.ürünler:
      item_ürün, item_miktar = item
      toplam += item_ürün.fiyat * item_miktar
    return toplam

  def sepet_görüntüle(self):
    if not self.ürünler:
      print("Sepet boş.")
    else:
      for item in self.ürünler:
        item_ürün, item_miktar = item
        print(f"{item_ürün.ad} - Miktar: {item_miktar} - Fiyat: {item_ürün.fiyat} TL")


# Örnek kullanım:
ürün1 = Ürün("Telefon", 5000, 10)
ürün2 = Ürün("Laptop", 10000, 5)
ürün3 = Ürün("Kulaklık", 500, 15)

sepet = Sepet()

# Ürün ekleme
sepet.ürün_ekle(ürün1, 3)
sepet.ürün_ekle(ürün2, 2)
sepet.ürün_ekle(ürün3, 5)

# Sepeti görüntüle
sepet.sepet_görüntüle()

# Toplam fiyat
print(f"Toplam Fiyat: {sepet.toplam_fiyat()} TL")

# Ürün silme
sepet.ürün_sil(ürün2)

# Sepeti tekrar görüntüle
sepet.sepet_görüntüle()
"""

"""
def solution(number_p):
  toplam =0
  if number_p <= 0:
    return 0
  else:
    for i in range(0,number_p):
      if (i % 3 and i % 5) == 0:
        toplam += i
      elif i % 3 == 0:
        toplam += i
      elif i % 5 == 0:
        toplam += i
      else:
        continue
    return toplam
number=int(input("bir sayı giriniz"))
ans=solution(number)
print(ans)
"""
"""
def duplicate_encode(word):
 encoded = []
 word=word.lower()
 for x in word:
    if word.count(x)>1:
      encoded.append(")")
    else:
      encoded.append("(")
 return "".join(encoded)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("success"))
print(duplicate_encode("(( @"))
"""

























