import pandas as pd

dunya = pd.read_csv("../dunya.csv", squeeze=True)

print("İlk 5 değer")
print(dunya.head())
print("*"*80)

print("Son 5 değer")
print(dunya.tail())
print("*"*80)

print("İl 3 Değer")
print(dunya.head(3))
print("*"*80)

print("İndex sayısı")
print(dunya.index)

print("Satır Ve Sutun Sayısı")
print(dunya.shape)
print("*"*80)

print("Columns")
print(dunya.columns)
print("*"*80)

print(dunya.info())
print("*"*80)