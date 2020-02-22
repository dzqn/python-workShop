import pandas as pd

x = [1, 2, 3, 4, 5]
print(pd.Series(x))

print("-" * 80)

y = ["ankara", "Antalya", "Rize"]
sehirler = pd.Series(y)
print(pd.Series(y))
print(sehirler.values)
print(sehirler.index)

print("-" * 80)

maas = {"ali": 80, "mehmet": 100}
print(pd.Series(maas))

print("-" * 80)


