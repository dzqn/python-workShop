# -*- coding: utf-8 -*-

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

milligelir = pd.read_csv("../milligelir.csv")
print(milligelir)
print("ilk 5 hane")
print(milligelir.head(5))
print("son 5 hane")
print(milligelir.tail(5))

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
