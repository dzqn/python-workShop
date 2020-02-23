
import pandas as pd

yillar = [2003, 2004, 2005, 2006]
gelir = [15000, 17000, 19000, 2000]

seri1 = pd.Series(data=gelir, index=yillar)
print(seri1)

print("*" * 80)

sayilar = pd.Series([1, 2, 4, 88, 55, 44])
print("Toplam: ", sayilar.sum())
print("En Büyük: ", sayilar.max())
print("En küçük: ", sayilar.min())
print("Çarpımlar: ", sayilar.product())
print("Ortalama: ", sayilar.mean())

print("*" * 80)

milligelir = pd.read_csv("../milligelir.csv", squeeze=True)
print(milligelir)
print("ilk 5 hane")
print(milligelir.head(5))
print("son 5 hane")
print(milligelir.tail(5))
print("En küçük gelirin indexi")
print(milligelir.idxmin())
print("En büyük gelirin indexi")
print(milligelir.idxmax())

print("-" * 80)

ulkeler = pd.read_csv("../ulke.csv", squeeze=True)
print(ulkeler)
print("Tip: ")
print(type(ulkeler))
print("Boyut: ")
print(len(ulkeler))
print("Sıralı Şekilde :")
sirali = sorted(ulkeler)
print(sirali)
print("Listeye Çevirme")
print(list(ulkeler))
print("Dictionary Hali:")
print(dict(ulkeler))

print("-" * 80)

print("Sıralı Ülkeler")
print(ulkeler.sort_values())
print("Sıralı gelir:")
print(milligelir.sort_values(ascending=False))

print("-" * 80)

print("ABD" in ulkeler.values)
print(ulkeler[0])
print(ulkeler[4:10])
print(ulkeler[5:])

print("-" * 80)

kitalar = pd.read_csv("../kita.csv", squeeze=True)
print(kitalar)
print("Her bir elemandan kaç tane var ?")
print(kitalar.value_counts())
print(kitalar.value_counts(ascending=True))
